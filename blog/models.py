from django.db import models
from django.utils import timezone


class Comic(models.Model):
    pic = models.ImageField(upload_to="comics")
    created_at = models.DateTimeField(auto_now_add=True)


class Mobile(models.Model):
    text = models.TextField()
