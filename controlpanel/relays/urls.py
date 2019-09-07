from django.urls import path
from . import views

app_name = 'relays'

urlpatterns = [
    path('', views.index, name='index'),
    path('updateState/<id>', views.updateState, name='updateState'),
]
