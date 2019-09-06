from django.conf.urls import url, include
from .views import news, news_detail, search_news, list_news_by_category

urlpatterns = [
    url(r'^$', news, name='news'),
    url(r'^search/$', search_news, name='search_news'),
    url(r'^category/(?P<slug>[-\w]+)/$', list_news_by_category, name='list_news_by_category'),
    url(r'^(?P<slug>[-\w]+)/$', news_detail, name='news_detail'),

]