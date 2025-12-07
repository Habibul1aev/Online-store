from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:main'))

    else:
        form = UserLoginForm()


    context = {
        'title': 'Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:main'))
    else:
        form = UserRegistrationForm()


    context = {
        'title': 'Регистрация',
        'form': form
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Кабинет'
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:main'))