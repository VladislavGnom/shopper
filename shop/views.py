from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def shop(request, category_id=None):
    all_categories = Category.objects.all()
    data_sort = request.GET.get('sort')

    if category_id:    
        if data_sort == "price-up":
            all_products = Product.objects.filter(category__pk=category_id, remainder__gte=1).order_by('price')
        elif data_sort == "price-down":
            all_products = Product.objects.filter(category__pk=category_id, remainder__gte=1).order_by('-price')
        else:
            all_products = Product.objects.filter(category__pk=category_id, remainder__gte=1)
    else:
        if data_sort == "price-up":
            all_products = Product.objects.filter(remainder__gte=1).order_by('price')
        elif data_sort == "price-down":
            all_products = Product.objects.filter(remainder__gte=1).order_by('-price')
        else:
            all_products = Product.objects.filter(remainder__gte=1)

    context = {
        'title': 'Магазин',
        'products': all_products,
        'categories': all_categories,
    }

    return render(request, 'shop/shop.html', context=context)


def detail_product(request, id):
    all_categories = Category.objects.all()
    product = get_object_or_404(Product, pk=id, remainder__gte=1)

    context = {
        'title': product.title,
        'product': product,
        'categories': all_categories,
    }

    return render(request, 'shop/product.html', context=context)



