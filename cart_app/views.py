from django.shortcuts import render

# Create your views here.


def cart_summary(request):
    return render(request, 'store_app/cart/cart.html')
