from django.shortcuts import render
from book.models import Book

def book(request):
    if request.method=="POST":
        title = request.POST['title']
        image = request.FILES.get('image')
        author = request.POST['author']
        publishyear = request.POST['publishyear']
        book = Book(title=title, image=image, author=author, publishyear=publishyear)
        book .save()   
    return render(request, "book_form.html")



# def author(request):
#     if request.method=="POST":
#         name = request.POST['name']
#         image = request.FILES.get('image')
#         fathername = request.POST['fathername']
#         publishedbooks = request.POST['publishedbooks']
#         author = Author(name=name, image=image, fathername=fathername, publishedbooks=publishedbooks)
#         author .save()
#     return render(request, "author_form.html")




