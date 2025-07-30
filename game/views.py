from django.shortcuts import render, HttpResponse
from game.models import Game  # ✅ your model

def game(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')  # ✅ safer way to access file
        message = request.POST.get('message')

        # ✅ Avoid using 'game' as variable name — it conflicts with function name
        game_obj = Game(name=name, image=image, message=message)
        game_obj.save()

    return render(request, 'game.html')
