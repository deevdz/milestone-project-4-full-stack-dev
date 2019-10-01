from django.conf.urls import url, include
from .views import all_products, single_product, list_products_by_category, shop

urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^department/(?P<slug>[-\w]+)/$', list_products_by_category, name='list_products_by_category'),
    url(r'^products/(?P<slug>[-\w]+)/$', single_product, name='single_product')
]