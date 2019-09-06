from django.db import models
from django.utils import timezone
from tinymce import HTMLField
from django.urls import reverse
from django.core.urlresolvers import reverse

class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=250, unique=True)
    blurb = models.TextField(default='',blank=True, null=True,)
    
    class Meta:
        ordering = ('title'),
        verbose_name = 'category',
        verbose_name_plural = 'categories'
        
    def get_absolute_url(self):
        return reverse('list_news_by_category', args=[self.slug])

    def __str__(self):
        return self.title

class Blog(models.Model):
    """
    Blog Posts to appear in the News section of the site
    """
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published','Published'),
        )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    content = HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')
    seo_title = models.CharField(max_length=250, blank=True, null=True)
    seo_description = models.CharField(max_length=250, blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    featured = models.BooleanField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('news_detail', args=[self.slug])
