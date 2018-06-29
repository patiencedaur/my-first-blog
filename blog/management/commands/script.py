from django.core.management.base import BaseCommand
import os, shutil
from mysite.settings import BASE_DIR
from blog.models import Comic

class Command(BaseCommand):
    help = "Move Deathbunnies A-Go-Go to site directory. Use once"

    def handle(self, **options):

        src = os.path.join(BASE_DIR, 'blog\comics') #исходная папка с комиксами
        file_set = os.listdir(path=src) # нашли все комиксы в папке

        print("Inserting comics...")
        for file_name in file_set: # для каждого имени файла в папке
            full_address = os.path.join(src, file_name) #полный исходный адрес файла
            destination = os.path.join(BASE_DIR, 'media\comics', file_name) #полный конечный адрес файла
            print("Moving to " + destination)
            shutil.copy2(full_address, destination) # переместить файлы в /media/comics
            Comic.objects.create(pic=destination) # создать соответствующие объекты в базе данных
