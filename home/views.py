from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog

# Create your views here.
def index(request):
    """A view that displays the Homepage"""
    featured = Blog.objects.filter(featured=True, status='published').order_by('-created_date')[:3]
    context = {
            'queryset': featured
            }
    return render(request, 'index.html', context)