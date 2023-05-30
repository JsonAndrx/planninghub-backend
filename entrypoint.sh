#!/bin/sh

echo "runing migration..."
python manage.py wait_for_db --settings=buildpro.settings.local
python manage.py migrate --settings=buildpro.settings.local

echo "creating superuser..."
python manage.py createsu --settings=buildpro.settings.local

echo "runing server..."
python manage.py runserver --settings=buildpro.settings.local