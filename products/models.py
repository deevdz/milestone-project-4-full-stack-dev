from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce import HTMLField
from django.urls import reverse
from django.core.urlresolvers import reverse

# Product Sizes
class ProductSize(models.Model):
    title = models.CharField(max_length=10)
    slug = models.SlugField(max_length=250, unique=True)
    
    def __str__(self):
        return self.title
    
#Product Colours
class ProductColour(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.title
        
#Product Category
class ProductCategory(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=250, unique=True)
    blurb = models.TextField(default='',blank=True, null=True,)
    
    class Meta:
        ordering = ('title'),
        verbose_name = 'category',
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title
    
#Products
class Product(models.Model):
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published','Published'),
        ('sold','Sold'),
        ('ended','Ended'),
        )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    content = HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')
    sku = models.CharField(max_length=30)
    seo_title = models.CharField(max_length=250, blank=True, null=True)
    seo_description = models.CharField(max_length=250, blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    featured = models.BooleanField()
    categories = models.ManyToManyField(ProductCategory)  
    colour = models.ManyToManyField(ProductColour) 
    size = models.ManyToManyField(ProductSize)
    buy_now = models.BooleanField(default=False)
    buy_now_price = models.FloatField()
    reserve = models.FloatField()
    time_ending = models.DateTimeField()
    
    def __str__(self):
        return self.title
    