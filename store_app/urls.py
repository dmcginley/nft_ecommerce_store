from django.urls import path
from . import views

from store_app .views import (
    HomeListView,
    ProductDetailView,
    # CreateCheckoutSessionView,
    # SuccessView, CancelView
)
app_name = 'store'


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('product/<slug:slug>/', ProductDetailView.as_view(),
         name='product_detail',),
    path('search/<slug:category_slug>/',
         views.category_list, name='category_list'),



    # path('', views.home, name='home'),
    # path('create-checkout-session/', CreateCheckoutSessionView.as_view(),
    #      name='create-checkout-session'),

    # path('checkout/', views.checkout, name='checkout'),

    # path('success/', SuccessView.as_view(), name='success'),
    # path('cancel/', CancelView.as_view(), name='cancel'),

]
