from django.shortcuts import render, get_list_or_404

from goods.models import Products, Categories


def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

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