from django.shortcuts import render

def home_view(request):
    context = { 'title': 'control-panel' }
    return render(request, 'pages/index.html', context)

