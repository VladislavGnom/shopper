from django.shortcuts import render, redirect
from .models import Cart
from shop.models import Product


def cart(request):
    cart = Cart.objects.filter(user=request.user)

    context = {
        'cart': cart,
    }

    return render(request, 'cart/cart.html', context=context)


def add_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = Cart.objects.create(user=request.user, product=product, amount=1, unit_price=product.price)

    cart.save()
    return redirect('cart')