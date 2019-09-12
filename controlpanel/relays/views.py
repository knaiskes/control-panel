from django.shortcuts import render, get_object_or_404, redirect
from .models import Relay
from .forms import UpdateStateForm
from django import forms
from mqtt.models import MqttRelay

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
    mqtt = MqttRelay(instance.name, instance.mqtt_topic )
    if form.is_valid():
        instance.state = instance.update_state(current_state)
        form.save()
        mqtt.send(instance.state)
        return redirect('relays:index')
    return render(request, 'relays/index.html')
