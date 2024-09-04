from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:category_id>', views.shop, name='shop'),
    path('product/<int:id>', views.detail_product, name='product')
]
