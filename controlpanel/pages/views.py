from django.shortcuts import render

def home_view(request):
    context = { 'title': 'home' }
    return render(request, 'pages/index.html', context)

