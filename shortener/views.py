from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ShortUrl
from .forms import NewShortUrlForm
from .utils import generate_short_url


def home(request):
    """Takes user input for url to shorten
    """
    return render(request, "shortener/home.html")


def create_short_url(request):
    """Shorten a url
    
    Takes the user input of an 
    Url & return a shortened version
    """
    if request.method == "POST":
        form = NewShortUrlForm(request.POST)
        if form.is_valid():
            shorturl = form.save(commit=False)
            shorturl.short_url = generate_short_url(10)
            shorturl.save()
            return redirect("view_short_url", shortURL=shorturl.short_url)
    else:   
        form = NewShortUrlForm
    return render(request, "shortener/create_short.html", {"form": form})


def open_short_url(request):
    """Open page to take user input 
    and redirect to short url page
    """
    if request.method == "POST":
        short_url = request.POST["short_url"]
        try:
            ShortUrl.objects.get(short_url=short_url)
            return redirect('view_short_url', shortURL=short_url)
        except ShortUrl.DoesNotExist:
            messages.error(request, f'This "{short_url}" short url does not exists')
            return render(request, "shortener/open_short_url.html")
        
    return render(request, "shortener/open_short_url.html")


def view_short_url(request, shortURL):
    
    shortUrl = ShortUrl.objects.get(short_url=shortURL)
    
    return render(request, "shortener/short_url.html", {"shortUrl": shortUrl})


def redirect_to_url(request, shortURL):
    
    shortUrl = ShortUrl.objects.get(short_url=shortURL)
    
    url_session_key = f"Visited: '{shortUrl.short_url}' already"
    if not request.session.get(url_session_key, False):
        shortUrl.times_visited +=1
        shortUrl.save()
        request.session[url_session_key] = True
        
    return redirect(shortUrl.original_url)