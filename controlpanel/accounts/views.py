from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('relays')
        else:
            #TODO: add error messages
            return redirect('login')

    else:
        return render(request, 'login.html')
