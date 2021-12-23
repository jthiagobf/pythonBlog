from django.contrib import admin

# Register your models here.


from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'update_at']
    list_filter = ['category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
