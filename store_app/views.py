from django.shortcuts import redirect, render, get_object_or_404

from store_app.models import Product, Category

from django.views.generic import (
    ListView, View
)


class HomeListView(ListView):
    model = Product
    template_name = 'store_app/home.html'
    context_object_name = 'products'


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'store_app/category.html', context)
