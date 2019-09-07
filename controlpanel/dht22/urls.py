from django.urls import path
from . import views

app_name = 'dht22'

urlpatterns = [
    path('', views.index, name='index'),
    path('records/<str:name>', views.records, name='records'),
]
