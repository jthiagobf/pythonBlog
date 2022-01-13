from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'), # url para ourta pagina chamada blog
    path('post/<int:id>/<slug:slug>', views.post_detail, name='post_detail')  

]
