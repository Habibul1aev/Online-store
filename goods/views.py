from unicodedata import category

from django.shortcuts import render

from goods.models import Products, Categories


def catalog(request):
    goods = Products.objects.all()

    context = {
        'title': 'Каталог',
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    prod = Products.objects.get(slug = product_slug)
    context = {
        'title': 'Продукт',
        'product': prod

    }
    return render(request, 'goods/product.html', context)