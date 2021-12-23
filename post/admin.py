from django.contrib import admin

# Register your models here.


from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)
