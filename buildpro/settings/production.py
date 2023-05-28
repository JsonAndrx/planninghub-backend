from .base import *
import os
from buildpro.logging import *
from dotenv import load_dotenv
import dj_database_url

load_dotenv(Path.joinpath(BASE_DIR, 'dotenv'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8b0mw9ghues#mqq4q7u$^8*ft0__7)!zo%cu4(i!+h)epxuh$_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": dj_database_url.parse('postgres://admin:6jZooPk4oTSfECFYCCQzIw2UJm93JiFK@dpg-chpqp2vdvk4goevpfjlg-a.oregon-postgres.render.com/postdb_swxm')
}

STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'