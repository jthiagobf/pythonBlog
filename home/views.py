from django.shortcuts import render, HttpResponse

# Create your views here.
from post.models import Post


def index(request):
    post_random = Post.objects.order_by('?')[:4]  # adiciona fotoa aleatoriamente

    context = {
        'post_random': post_random
    }
    return render(request, 'index.html', context)
