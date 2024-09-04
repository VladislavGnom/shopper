from django.shortcuts import render, redirect
from .models import Cart
from shop.models import Product, Category


def cart(request):
    all_categories = Category.objects.all()
    cart = Cart.objects.filter(user=request.user)

    context = {
        'cart': cart,
        'categories': all_categories,
    }

    return render(request, 'cart/cart.html', context=context)


def add_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    is_product_in_cart = True if Cart.objects.filter(product__id = product_id) else False
    if is_product_in_cart:
        cart = Cart.objects.get(user=request.user, product=product)
        cart.amount += 1
    else:
        cart = Cart.objects.create(user=request.user, product=product, amount=1, unit_price=product.price)

    cart.save()
    return redirect('cart')