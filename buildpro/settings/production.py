from .base import *
import os
from buildpro.logging import *
from dotenv import load_dotenv
import dj_database_url

load_dotenv(Path.joinpath(BASE_DIR, 'dotenv'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'