from django.conf.urls import url
from . import views
urlpatterns = [
# view под названием post_list связывается с пустым адресом,
# ему присваивается название post_list
    url(r'^$', views.post_list, name='post_list'),
]
