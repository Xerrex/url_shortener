from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """Takes user input for url to shorten
    """
    return render(request, "shortener/home.html")
