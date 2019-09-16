from django import forms
from tinymce import TinyMCE
from .models import ProductSize, ProductColour, ProductCategory, Product

class ProductSizeForm(forms.ModelForm):
    class Meta:
        model = ProductSize
        fields = ('title', 'slug', )

class ProductColourForm(forms.ModelForm):
    class Meta:
        model = ProductColour
        fields = ('title', 'slug', )
        
class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('title', 'slug', 'blurb' )        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'slug', 'content','status', 'sku', 'seo_title',
        'seo_description', 'tag', 'image','featured','categories', 'colour',
        'size', 'buy_now','buy_now_price', 'reserve','time_ending',)