from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .forms import ProductSizeForm, ProductColourForm, ProductCategoryForm, ProductForm
from .models import ProductSize, ProductColour, ProductCategory, Product
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def list_products_by_category(request, slug):
    shop_categories = ProductCategory.objects.all()
    category_count = get_category_count()
    product_list = Product.objects.filter(status='published')
    
    if slug:
        product_category = get_object_or_404(ProductCategory, slug=slug)
        product_list = product_list.filter(categories=product_category).distinct()
    
    context = {
        'shop_categories': shop_categories,
        'product_queryset': product_list,
        'product_category': product_category,
        'category_count': category_count
    }
    return render(request,'shop_category.html', context )

# Count the number of posts in each category
def get_category_count():
    queryset = Product \
        .objects \
        .filter(status='published') \
        .values('categories__title', 'categories__slug') \
        .annotate(Count('categories__title'))
    return queryset

# Create your views here.
def shop(request):
    """A view that displays all the Products on a Shop Page"""
    category_count = get_category_count()
    product_list = Product.objects.filter(status='published').order_by('-created_date')
    count_published = product_list.count()
    paginator = Paginator(product_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    
    if product_list:
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
    return render(request, 'shop.html', context)


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'all_products.html', context)
    
def single_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.views += 1
    product.save()

    context = {
        'product': product,
    }
    
    return render(request, 'product.html', context)
