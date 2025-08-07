from django.urls import path
from .views import car

urlpatterns = [
    path('', car, name='car'),
]