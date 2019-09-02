from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog

# Create your views here.
def index(request):
    """A view that displays the index page"""
    featured = Blog.objects.filter(featured=True)
    context = {
            'object_list': featured
            }
    return render(request, 'index.html', context)