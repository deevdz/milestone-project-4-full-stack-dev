from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

# Searching the News
def search(request):
    queryset = Blog.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tag__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'searchnews.html', context)


# Count the number of posts in each category
def get_category_count():
    queryset = Blog \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset

# Create your views here.
def news(request):
    """A view that displays all the News Stories on a News Page"""
    category_count = get_category_count()
    news_items = Blog.objects.order_by('-created_date')
    paginator = Paginator(news_items, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'category_count' : category_count
    }
    return render(request, 'news.html', context)

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
    
    try:
        next_news = news.get_next_by_created_date()
    except Blog.DoesNotExist:
        next_news = None

    try:
        previous_news = news.get_previous_by_created_date()
    except Blog.DoesNotExist:
        previous_news = None
    
    context = {
        'news': news,
        'next_news': next_news,
        'previous_news': previous_news
    }
    
    return render(request, 'newsitem.html', context)