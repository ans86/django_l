from django.shortcuts import render, redirect
from .models import Author

def author(request):
    if request.method == "POST":
        print("Form data:", request.POST)
        name = request.POST['name']
        author = Author(name=name)



        author.save()
        return redirect('author')

    return render(request, 'author_form.html')


