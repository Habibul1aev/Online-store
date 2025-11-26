from django.shortcuts import render

from goods.models import Categories


def main(request):
    categories = Categories.objects.all()

    context = {
        'title': "Главная",
        'categories': categories,
    }
    return render(request, 'main/body.html', context)

def about(request):


    context = {
        'title': "О нас"
    }
    return render(request, 'main/about.html', context)
