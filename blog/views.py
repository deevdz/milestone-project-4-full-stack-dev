from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def news(request):
    """A view that displays all the News Stories on a News Page"""
    news_items = Blog.objects.order_by('-created_date')
    return render(request, 'news.html', {'news_items': news_items})

def news_detail(request, pk):
    """
    Create a view that returns a single
    News Item based on the post ID (pk) and
    render it to the 'news_item.html' template.
    Or return a 404 error if the post is
    not found
    """
    news = get_object_or_404(Blog, pk=pk)
    news.views += 1
    news.save()
    return render(request, 'newsitem.html', {'news': news})