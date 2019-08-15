from django.shortcuts import render
from .models import Relay

def index(request):
    context = {
        'relays': Relay.objects.all(),
        'title': 'Available Relays'
    }
    return render(request, 'relays/index.html', context)
