from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('records/<str:name>', views.records, name='records'),
]
