from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name='main'),
    path('product/<int:id>', views.detail_product, name='product')
]
