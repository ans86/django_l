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
from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('aot/', views.aot_view, name='aot'),
    path('home', views.home_view, name="home"),
    path('seasons', views.seasons_view, name="seasons"),
    path('characters/', views.characters_view, name="characters"),
    path('about/', views.about_view, name="about"),
    # Contact app urls
    path('contact/', include('contact.urls')),
]
