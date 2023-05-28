#!/bin/sh

echo "runing collectstatic..."
python manage.py collectstatic --no-input --settings=buildpro.settings.production

echo "runing migration..."
python manage.py wait_for_db --settings=buildpro.settings.production
python manage.py migrate --settings=buildpro.settings.production

echo "runing server..."
gunicorn --env DJANGO_SETTINGS_MODULE=buildpro.settings.production buildpro.wsgi:application