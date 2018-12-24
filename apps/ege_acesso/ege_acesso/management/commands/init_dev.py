from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import Usuario


class Command(BaseCommand):
    help = "My shiny new management command."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        if not settings.DEBUG:
            print("init_dev are project to dev environment")
            
        su = Usuario.objects.filter(is_superuser=True).first()
        if su is None:
            print("Create your superuser before init dev environment")
