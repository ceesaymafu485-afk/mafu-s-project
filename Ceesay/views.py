from django.shortcuts import render

def home(request):
    return render(request, 'Ceesay/home.html')

def about(request):
    return render(request, 'Ceesay/about.html')