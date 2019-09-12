from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .forms import CommentForm, BlogForm
from .models import Blog, Category, Comment
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

# Searching the News
def search_news(request):
    queryset = Blog.objects.filter(status = 'published')
    query = request.GET.get('q')
    
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tag__icontains=query)
        ).distinct()
    else:
        queryset = Blog.objects.filter(status = 'published')
        
    category_count = get_category_count()
    context = {
        'queryset': queryset,
        'category_count': category_count
    }
    return render(request, 'searchnews.html', context)

def list_news_by_category(request, slug):
    categories = Category.objects.all()
    category_count = get_category_count()
    news_items = Blog.objects.filter(status='published')
    
    if slug:
        category = get_object_or_404(Category, slug=slug)
        news_items = news_items.filter(categories=category).distinct()
    
    context = {
        'categories': categories,
        'queryset': news_items,
        'category': category,
        'category_count': category_count
    }
    return render(request,'categorydetail.html', context )

# Count the number of posts in each category
def get_category_count():
    queryset = Blog \
        .objects \
        .filter(status='published') \
        .values('categories__title', 'categories__slug') \
        .annotate(Count('categories__title'))
    return queryset

# Create your views here.
def news(request):
    """A view that displays all the News Stories on a News Page"""
    category_count = get_category_count()
    news_items = Blog.objects.filter(status='published').order_by('-created_date')
    count_published = news_items.count()
    paginator = Paginator(news_items, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    
    if news_items:
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'category_count' : category_count,
        'count_published': count_published,
    }
    return render(request, 'news.html', context)

def news_detail(request, slug):
    """
    Create a view that returns a single
    News Item based on the post slug and
    render it to the 'news_item.html' template.
    Or return a 404 error if the post is
    not found
    """
    news = get_object_or_404(Blog, slug=slug)
    news.views += 1
    news.save()
    category_count = get_category_count()

    form = CommentForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.blog = news
            form.save()
            return redirect(reverse("news-detail", kwargs={
                'slug': news.slug
            }))    
    
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
        'previous_news': previous_news,
        'category_count' : category_count,
        'form' : form
    }
    
    return render(request, 'newsitem.html', context)