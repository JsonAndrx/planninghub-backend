from django.core.management import BaseCommand
from django.db import connection
from django.db.utils import OperationalError
from time import sleep

class Command(BaseCommand):
    hel = 'Wait for database connection'

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database')
        db_conn = False

        while not db_conn:
            try:
                c = connection.cursor()
                c.execute('SELECT 1')
                db_conn = True
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second')
                sleep(1)

        self.stdout.write(self.style.SUCCESS('Databe available'))