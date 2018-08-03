from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
# when the view "comic_list" sees an empty url, it assigns it the name "comic_list"
    url(r'^$', views.comic_list, name='comic_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
