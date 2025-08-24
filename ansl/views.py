from django.http import HttpResponse
from django.shortcuts import render
from game.models import Game
from laptop.models import Laptop
from car.models import Car
from book.models import Book


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

def laptops_view(request):
    laptops = Laptop.objects.all()
    context = {
        "laptops": laptops
    }
    return render(request, 'laptops.html', context)

def cars(request):
    cars = Car.objects.all()
    context = {
        "cars": cars
    }
    return render(request, 'cars.html', context)

def author_form_view(request):
     return render(request, 'author_form.html')


def books_view(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, 'books.html', context)

def author_view(request):
    author = Book.objects.all()
    context = {
        "authors": author
    }
    return render(request, 'author.html', context)

def anime_list(request):
    from anime.models import Anime
    animes = Anime.objects.all()
    return render(request, "anime_list.html", {"animes": animes})