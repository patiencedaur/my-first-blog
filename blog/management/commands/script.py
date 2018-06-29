from django.core.management.base import BaseCommand
import os, shutil
from mysite.settings import BASE_DIR
from blog.models import Comic

class Command(BaseCommand):
    help = "Move Deathbunnies A-Go-Go to site directory. Use once"

    def handle(self, **options):

        src = os.path.join(BASE_DIR, 'blog\comics') #initial folder
        file_set = os.listdir(src) # find all comics in folder

        print("Inserting comics...")
        for file_name in file_set: # for every comic in initial folder
            full_address = os.path.join(src, file_name) #full initial address
            destination = os.path.join(BASE_DIR, 'media\comics', file_name) #full destination address
            print("Moving to " + destination)
            shutil.copy2(full_address, destination) # move files to /media/comics
            Comic.objects.create(pic=destination) # create objects in database
