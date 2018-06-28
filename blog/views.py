from django.shortcuts import render
from django.utils import timezone
from .models import Mobile, Comic

def comic_list(request):
    comics = Comic.objects.order_by('pic')
    print(comic_list)
    return render(request, 'blog/comic_list.html', {'comics': comics})

def mobile_page(request):
    mpage = Mobile.objects.all()
    return render(request, 'blog/mobile.html', {})
