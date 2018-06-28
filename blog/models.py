from django.db import models
from django.utils import timezone


class Comic(models.Model):
    pic = models.ImageField(upload_to="comics")


class Mobile(models.Model):
    text = models.TextField()
