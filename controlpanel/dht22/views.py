from django.shortcuts import render
from .models import Dht22

def index(request):
    dht22_list = Dht22.objects.all()

    context = {
        'dht22_list': dht22_list,
        'title': 'Available Dht22 sensors',
    }

    return render(request, 'dht22/index.html', context)
