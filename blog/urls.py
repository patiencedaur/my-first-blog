from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
# view под названием comic_list связывается с пустым адресом,
# ему присваивается название post_list
    url(r'^$', views.comic_list, name='comic_list'),
    url('mobile', views.mobile_page, name='mobile_page')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
