from django.urls import path
from . import views

urlpatterns = [
    path("form", views.book, name="book"),  
    path("author_form/", views.create_author, name="author_form"),  # independent author form
]
