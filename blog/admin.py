from django.contrib import admin
from .models import Category, Blog, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'blurb')
    prepopulated_fields = {'slug': ('title',)}

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','published', 'status', 'featured')
    list_filter = ('published','featured')
    search_fields = ('title', 'content', 'tag')
    prepopulated_fields = {'slug': ('title',)}
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'blog', 'timestamp')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
