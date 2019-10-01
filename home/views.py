from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog
from products.models import ProductCategory, Product
import random

# Create your views here.
def index(request):
    """A view that displays the Homepage"""
    featured = Blog.objects.filter(featured=True, status='published').order_by('-created_date')[:3]
    product_categories = ProductCategory.objects.order_by('?')[:4]
    context = {
            'queryset': featured,
            'category_queryset' : product_categories
            }
    return render(request, 'index.html', context)