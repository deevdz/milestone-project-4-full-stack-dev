from django.db import models
from django.utils import timezone
from tinymce import HTMLField
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=30)
    blurb = models.TextField(default='')
    def __str__(self):
        return self.title

class Blog(models.Model):
    """
    Blog Posts to appear in the News section of the site
    """
    title = models.CharField(max_length=200)
    content = HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    featured = models.BooleanField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={
        'pk': self.pk
        })
