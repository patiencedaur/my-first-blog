from django.core.management.base import BaseCommand
import os
from mysite.settings import BASE_DIR
from blog.models import Comic

class Command(BaseCommand):
    help = "Create database objects. Use once"

    def handle(self, **options):

        src = os.path.join(BASE_DIR, 'media', 'comics') #folder with comics
        file_set = os.listdir(src) # find all comics in folder

        print("Creating Comic objects in database...")

        for file_name in file_set: # for every comic in initial folder
            destination = os.path.join(src, file_name) #full destination address
            relative_path = '/' + '/'.join(destination.split('/')[-3:])
            Comic.objects.create(pic=relative_path) # create objects in database
            print("site path: " + relative_path)
