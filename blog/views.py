from django.shortcuts import render
from .models import Mobile, Comic
from .middleware.detectmobilebrowser import process_request

def comic_list(request):
    comics = Comic.objects.order_by('pic')
    print(comic_list)
    return render(request, 'blog/comic_list.html', {'comics': comics})

def mobile_page(request):
    if process_request(request) == True:
        return render(request, 'blog/mobile.html', {})
