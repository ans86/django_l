from django.urls import path
from .views import car, car_detail,car_edit,car_delete, car_review

urlpatterns = [
    path('form', car, name='car'),
    path('car/review<int:id>/', car_review, name='car_review'),
    path("detials/<int:id>/", car_detail, name="car_detail"),
    path('/edit/<int:id>/', car_edit, name='car_edit'),
    path('/delete/<int:id>/', car_delete, name='car_delete'),
]