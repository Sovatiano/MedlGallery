from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Function import models

# Create your views here.

authentication = [1]


@login_required(login_url='login')
def welcome(request):
    return render(request, 'firstTemplate.html')


@login_required(login_url='login')
def mywelcome(request):
    return render(request, 'PersonalTemplate.html', {'name': 'Vlad'})


def loginpage(request):
    if request.method == 'POST':
        loginn = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=loginn, password=password)
        if not request.POST.get('remember'):
            request.session.set_expiry(0)

        if user is not None:
            print(1)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')