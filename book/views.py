from django.shortcuts import render, redirect
from .models import Book, Authors, Country

def book(request):
    if request.method == "POST":
        title = request.POST['title']
        image = request.FILES.get('image')
        author_id = request.POST['author']
        author = Authors.objects.get(id=author_id)
        publishyear = request.POST['publishyear']
        
        Book.objects.create(
            title=title,
            image=image,
            author=author,
            publishyear=publishyear
        )
        return redirect("books")

    authors = Authors.objects.all()
    return render(request, "book_form.html", {"authors": authors})


def create_author(request):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.FILES.get("image")
        publishedbooks = request.POST.get("publishedbooks")
        dateofbirth = request.POST.get("dateofbirth")
        country_id = request.POST.get("country")

        country = Country.objects.get(id=country_id)

        Authors.objects.create(
            name=name,
            image=image,
            country=country,
            dateofbirth=dateofbirth, 
            publishedbooks=publishedbooks   # naya line
        )
        return redirect("author_form")

    countries = Country.objects.all()

    return render(request, "author_form.html", {"countries": countries})

