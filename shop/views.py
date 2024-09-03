from django.shortcuts import render, get_object_or_404
from .models import Product


def shop(request):
    all_products = Product.objects.filter(remainder__gte=1)

    context = {
        'title': 'Магазин',
        'products': all_products,
    }

    return render(request, 'shop/shop.html', context=context)


def detail_product(request, id):
    product = get_object_or_404(Product, pk=id, remainder__gte=1)

    context = {
        'title': product.title,
        'product': product,
    }

    return render(request, 'shop/product.html', context=context)
