from django.shortcuts import render
from .models import Relay
from .forms import UpdateStateForm
from django import forms

def index(request):
    context = {
        'relays': Relay.objects.all(),
        'title': 'Available Relays'
    }
    return render(request, 'relays/index.html', context)

def updateState(request):
    form = UpdateStateForm()
    relays_list = Relay.objects.all()
    context = {
            'form': form,
            'relays_list': relays_list
    }

    if request.method == 'POST':
        form = UpdateStateForm(request.POST or None)
        if form.is_valid():
            state = request.POST.get('state', '')
            print(state)
    return render(request, 'relays/updateState.html', context)
