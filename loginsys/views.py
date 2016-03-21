from django.shortcuts import render, redirect
from django.contrib import auth

def login(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {
              'login_error': "Пользователь не найден",
              })
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
