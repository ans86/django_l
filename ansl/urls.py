"""
URL configuration for ansl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('gam/', views.gam_view, name='gam'),
    path('home', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('form/', views.form_view, name="form" ),
    path('laptops/', views.laptops_view, name="laptops" ),
    path('cars/', views.cars_view, name="cars" ),
    #Contact app urls
    path('contact_form/', include('contact.urls')),
    path('game_form/', include('game.urls')),
    path('laptop_form/', include('laptop.urls')),
    path('cars_form/', include('car.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
