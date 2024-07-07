from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("portfolio/", views.portfolio, name='portfolio'),
    path("abouts/", views.abouts, name='abouts'),
    
]