from django.urls import path
from .views import author, book

urlpatterns = [
    path('', author, name='author'),
    path('', book, name='book'),
]
