from django.contrib import admin

# Register your models here.


from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('title',)} # add slug automaticamente


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'update_at', 'image_table']
    readonly_fields = ('image_table',)
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)} #add slug automaticamente



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
