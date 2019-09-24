from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    context = { 'title': 'control-panel' }
    return render(request, 'pages/index.html', context)

@login_required
def dashboard_view(request):
    context = { 'title': 'dashboard' }
    return render(request, 'pages/dashboard.html', context)
