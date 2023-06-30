from django.urls import path
from . import views

# from cart_app .views import (

# )


app_name = 'cart'

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),

    path('add/', views.cart_add, name='cart_add'),
    path('update/', views.cart_update, name='cart_update'),
    path('delete/', views.cart_delete, name='cart_delete'),
]
