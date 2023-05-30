from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        if User.objects.filter(username='admin').exists():
            return 'Superuser already exist'
        User.objects.create_superuser(
            username='admin',
            password='adminyeison123'
        )
        return 'Superuser has been created'
