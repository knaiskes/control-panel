from django.shortcuts import render, get_object_or_404
from .models import Relay
from .forms import UpdateStateForm
from django import forms

def index(request):
    context = {
        'relays': Relay.objects.all(),
        'title': 'Available Relays'
    }
    return render(request, 'relays/index.html', context)

def updateState(request, id):
    form = UpdateStateForm()
    relays_list = Relay.objects.all()
    context = {
            'form': form,
            'relays_list': relays_list
    }
    if request.method == 'POST':
        instance = get_object_or_404(Relay, id=id)
        form = UpdateStateForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            state = request.POST.get('state', '')
            print(state)
    return render(request, 'relays/updateState.html', context)
