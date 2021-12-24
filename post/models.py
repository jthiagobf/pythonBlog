from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)  # datas automaticas
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):   # altera o nome da categoria automaticamente na parte do admin
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(unique=True, null=False)
    subtitle = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='images/', blank=True)
    text = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) # data automatica

    def __str__(self): # altera o nome dos posts automaticamente na parte do admin
        return self.title


    def image_table(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return mark_safe('<p>Sem imagem</p>')





