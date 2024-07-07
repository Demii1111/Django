from django.shortcuts import render
from django.urls import path 

# Create your views here.
def home (request) :
    return render(request,"home.html")

def portfolio (request) :
    return render(request,"portfolio.html")

def abouts (request) :
    return render(request,"abouts.html")

