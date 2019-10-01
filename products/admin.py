from django.contrib import admin
from .models import ProductColour,ProductSize, ProductCategory, ProductCondition, Product

class ProductColourAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    
class ProductConditionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}    
    
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'featured')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(ProductColour, ProductColourAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)
admin.site.register(ProductCondition, ProductConditionAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)