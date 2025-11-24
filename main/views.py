from django.shortcuts import render

def main(request):


    context = {
        'title': "Главная"
    }
    return render(request, 'main/body.html', context)

def about(request):


    context = {
        'title': "О нас"
    }
    return render(request, 'main/about.html', context)
