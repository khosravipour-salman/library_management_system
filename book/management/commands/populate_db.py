from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounting.models import CustomUserModel


class Command(BaseCommand):
    help = 'Populates database with dummy-data.'

    def handle(self, *args, **kwargs):
        self.stdout.write("test!")
        