from django.shortcuts import render, get_object_or_404
from .models import Dht22, Record

def index(request):
    dht22_list = Dht22.objects.all()

    context = {
        'dht22_list': dht22_list,
        'title': 'Available Dht22 sensors',
    }

    return render(request, 'dht22/index.html', context)

def records(request, name):
    records = Record.objects.filter(name=name)
    context = {
            'records': records,
            'title': 'Dht22 records',
            'name': name,
    }
    return render(request, 'dht22/records.html', context)
