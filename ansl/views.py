from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'aot.html')

def aot_view(request):
#  return HttpResponse("Hello, World!")
     return render(request, 'aot.html')

def home_view(request):
     return render(request, 'home.html')

def seasons_view(request):
     return render(request, 'seasons.html')

def characters_view(request):
     return render(request, 'characters.html')

def about_view(request):
     return render(request, 'about.html')
