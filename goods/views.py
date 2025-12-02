
from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404, get_object_or_404

from goods.models import Products, Categories


def catalog(request, category_slug = None):
    category = get_object_or_404(Categories, slug = category_slug)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category=category, is_publish=True)

    min_price = request.GET.get('from_price', None)
    max_price = request.GET.get('to_price', None)
    order_by = request.GET.get('order_by', None)
    on_sale = request.GET.get('on_sale', None)

    if min_price and max_price:
        if min_price <= max_price:
            goods = goods.filter(price__range=(min_price, max_price))
        else:
            goods = goods.filter(price__range=(max_price, min_price))
    elif min_price:
        goods = goods.filter(price__gte = min_price)
    elif max_price:
        goods = goods.filter(price__lte = max_price)
    if on_sale:
        goods = goods.filter(discount__gt = 0)
    if order_by:
        goods = goods.order_by(order_by)

    page = request.GET.get('page', 1)
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Каталог',
        'goods': current_page,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    prod = Products.objects.get(slug = product_slug)
    context = {
        'title': 'Продукт',
        'product': prod

    }
    return render(request, 'goods/product.html', context)