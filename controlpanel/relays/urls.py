from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('updateState/<id>', views.updateState, name='updateState'),
]
