from django.http import HttpResponse
from django.shortcuts import render
from game.models import Game
from laptop.models import Laptop

def index(request):
    return render(request, 'gam.html')

def gam_view(request):
#  return HttpResponse("Hello, World!")
     return render(request, 'gam.html')

def home_view(request):
    games = Game.objects.all()
    context = {
        "games": games
    }
    return render(request, 'home.html', context)

def about_view(request):
     return render(request, 'about.html')

def form_view(request):
     return render(request, 'form.html')

def laptops_view(request):
    laptops = Laptop.objects.all()
    context = {
        "laptops": laptops
    }
    return render(request, 'laptops.html', context)