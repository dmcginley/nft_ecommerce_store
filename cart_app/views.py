from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from store_app.models import Product
from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    return render(request, 'store_app/cart/cart.html', {'cart': cart})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()

        # response = JsonResponse({'qty': cartqty})
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})

        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart.update(product=product_id, qty=product_qty)
        # print(product_id)
        # print(product_qty)
        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        # total = cart.total_price()

        response = JsonResponse(
            {'qty': cartqty, 'subtotal': carttotal})
        # response = JsonResponse({'Success': True})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)
        cartqty = cart.__len__()
        carttotal = cart.get_total_price()

        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
        return response
