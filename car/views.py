from django.shortcuts import render , HttpResponse
from car.models import Car


def car(request):
    if request.method=="POST":
        name = request.POST['name']
        image = request.FILES.get('image')
        model = request.POST['model']
        engine = request.POST['engine']
        enginepower = request.POST['enginepower']
        price = request.POST['price']
        madein = request.POST['madein']
        topspeed = request.POST['topspeed']
        car = Car(name=name, image=image, model=model, engine=engine, enginepower=enginepower, price=price, madein=madein, topspeed=topspeed)
        car.save()
    return render(request, "cars_form.html")