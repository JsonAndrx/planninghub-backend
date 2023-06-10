#!/bin/sh

echo "conect database..."
python manage.py wait_for_db --settings=buildpro.settings.local

echo "running migrations.."
python manage.py makemigrations --settings=buildpro.settings.local
python manage.py migrate --settings=buildpro.settings.local

echo "creating superuser..."
python manage.py createsu --settings=buildpro.settings.local

echo "runing server..."
python manage.py runserver --settings=buildpro.settings.local 0.0.0.0:8000