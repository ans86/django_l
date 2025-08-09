from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from game.models import Game

def game(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        details = request.POST.get('details')

        
        game_obj = Game(name=name, image=image, details=details)
        game_obj.save()

    return render(request, 'game.html')


def game_list(request):
    games=Game.objects.all()
    return render(request, 'home.html',games=games)

def game_list(request):
    game = Game.objects.all().order_by('-timeStamp')
    return render(request, 'game.html', {'games': game})


def game_detail(request, id):
    game_detail = get_object_or_404(Game, id=id)
    return render(request, 'game_detail.html', {'game_detail': game_detail})


def game_edit(request, id):
    game = get_object_or_404(Game, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        details = request.POST.get('details')

        if not name or not details:
            return render(request, 'game_edit.html', {
                'game': game,
                'error': 'Please fill in all fields.'
            })

        game.name = name
        game.details = details

        if image:
            game.image = image

        game.save()
        return redirect('game_detail', id=game.id)

    return render(request, 'game_edit.html', {'game': game})

def game_delete(request, id):
    game = get_object_or_404(Game, id=id)
    game.delete()
    return redirect('games')