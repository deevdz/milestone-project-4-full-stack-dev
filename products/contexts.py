from .models import ProductCategory

def nav_product_categories(context):
    return {'cats': ProductCategory.objects.all()}