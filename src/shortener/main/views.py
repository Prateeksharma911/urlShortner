from django.shortcuts import render, redirect
from django.http import HttpResponse
import pyshorteners
from main.manager import url_manager
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def shorten_post(request):
    return shorten(request, request.POST['url'])

def redirect_hash(request, url_hash):
    original_url = url_manager.load_url(url_hash).original_url
    return redirect(original_url)

def shorten(request, url):
    try:
        shortened_url_hash = url_manager.shorten(url)
        shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
        return render(request, 'main/link.html', {'shortened_url': shortened_url})

        shortener = pyshorteners.Shortener()
        shortened_url = shortener.clckru.short(url)
        return HttpResponse(f'Shortened URL: <a href="{shortened_url}">{shortened_url}</a>')
    except Exception as e:
        return HttpResponse(str(e))
        

