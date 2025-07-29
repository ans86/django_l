from django.shortcuts import render , HttpResponse
from contact.models import Contact


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        username = request.POST['username']
        email=request.POST['email']
        meassage=request.POST['message']
        contact = Contact(name=name, email=email, message=meassage, username=username)
        contact.save()
    return render(request, "contact.html")