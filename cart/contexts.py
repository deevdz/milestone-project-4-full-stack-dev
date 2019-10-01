from django.shortcuts import get_object_or_404
from products.models import Product

#Allow Cart to be available across all pages on the site
def cart_contents(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 1
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += product_count * product.buy_now_price
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}