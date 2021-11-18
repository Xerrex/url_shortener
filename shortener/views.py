from django.http import HttpResponse


def home(request):
    """Takes user input for url to shorten
    """
    return HttpResponse("welcome home")
