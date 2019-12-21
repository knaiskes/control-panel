from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
