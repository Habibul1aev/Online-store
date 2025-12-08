from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


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

@login_required()
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data = request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'Кабинет',
        'form': form
    }

    return render(request, 'users/profile.html', context)

@login_required()
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:main'))