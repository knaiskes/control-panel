from django.shortcuts import render, get_object_or_404, redirect
from .models import Relay
from .forms import UpdateStateForm
from django import forms

def index(request):
    relays_list = Relay.objects.all()
    form = UpdateStateForm()
    context = {
        'relays_list': relays_list,
        'title': 'Available Relays',
        'form': form
    }
    return render(request, 'relays/index.html', context)

def updateState(request, id):
    instance = get_object_or_404(Relay, id=id)
    form = UpdateStateForm(request.POST or None, instance=instance)
    current_state = instance.state
    if form.is_valid():
        instance.update_state(current_state)
        form.save()
        return redirect('index')
    return render(request, 'relays/index.html')
