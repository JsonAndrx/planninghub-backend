from .base import *
import os
from buildpro.logging import *
from dotenv import load_dotenv
import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

load_dotenv(Path.joinpath(BASE_DIR, 'dotenv'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
}



sentry_sdk.init(
    dsn="https://ef260c4b1cc246cb969678b9e1eb5192@o4505250926362625.ingest.sentry.io/4505264163586048",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'