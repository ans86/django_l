from django.urls import path
from .views import contact

urlpatterns = [
    path('form', contact, name='contact'),
]