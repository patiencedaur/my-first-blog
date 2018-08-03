from django.shortcuts import render
from django.utils import timezone
from .models import Comic


def comic_list(request):
    comics = Comic.objects.order_by('pic')
    print(comic_list)
    return render(request, 'blog/comic_list.html', {'comics': comics})

