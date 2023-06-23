from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from store_app.models import Product
from .cart import Cart


def cart_summary(request):
    return render(request, 'store_app/cart/cart.html')


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)
        response = JsonResponse({'qty': product_qty})
        return response
