from django.urls import path
from . import views


urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('add_product_to_cart/<int:product_id>', views.add_product, name='add-product-to-cart'),
]

