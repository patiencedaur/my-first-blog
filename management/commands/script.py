from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Print 'Hello World' in the command line"

    def handle(self, **options):
        self.stdout.write("Hello World!", ending='')
