from django.shortcuts import render, redirect
from .models import Author, Book

def author_form(request):
    if request.method == "POST":
        name = request.POST['name']
        author = Author(name=name)
        author.save()
        return redirect('author_form')

    return render(request, 'author_form.html')


def book_form(request):
    authors = Author.objects.all()  # dropdown ke liye

    if request.method == "POST":
        name = request.POST['name']
        image = request.FILES.get('image')
        publishyear = request.POST['publishyear']
        author_id = request.POST['author']  # dropdown se aaya id

        author = Author.objects.get(id=author_id)
        book = Book(name=name, image=image, publishyear=publishyear, author=author)
        book.save()

        return redirect('book_form')

    return render(request, 'book_form.html', {'authors': authors})
