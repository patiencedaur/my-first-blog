from django.db import models

class Comic(models.Model):
    pic = models.ImageField(upload_to="comics")