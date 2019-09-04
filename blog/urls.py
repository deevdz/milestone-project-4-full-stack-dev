from django.conf.urls import url, include
from .views import news, news_detail, search

urlpatterns = [
    url(r'^$', news, name='news'),
    url(r'^(?P<pk>\d+)/$', news_detail, name='news_detail'),
    url(r'^search/', search, name='search_news'),
]