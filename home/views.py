from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.
from .models import Contact

from .forms import ContactForm

from post.models import Post, Category, Comment


def index(request):
    post_random = Post.objects.order_by('?')[:4]  # adiciona fotos aleatoriamente
    post_latest = Post.objects.order_by('id')[:3] #ordena posts pelo id
    category = Category.objects.all()

    context = {
        'post_random': post_random,
        'post_latest': post_latest,
        'category': category

    }
    return render(request, 'index.html', context)


def blog(request):
    post = Post.objects.all()
    category = Category.objects.all()
    post_latest = Post.objects.order_by('id')[:3]

    paginator = Paginator(post, 4)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'category': category,
        'post_latest': post_latest,

    }

    return render(request, 'pages/blog.html', context)  # pagina blog


def post_detail (request, id, slug):
    post = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post_id=id, status='Lido')
    return render(request, 'pages/post_detail.html', {'post': post, 'comments': comments})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']

            data.save()
            return HttpResponseRedirect('/contact/')
    form = ContactForm
    context = {
        'form': form
    }

    return render(request, 'pages/contact.html', context)


def about(request):
    return render(request, 'pages/about.html')

