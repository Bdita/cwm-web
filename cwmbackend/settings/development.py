import os
import sys

from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
SECRET_KEY = os.environ.get('CWMBACKEND_SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cwmdatabase',
        'USER': 'cwmdatabaseuser',
        'PASSWORD': os.environ.get('CWMDATABASE_PASSWORD', ''),
        'HOST': 'localhost',
        'PORT': '',
    }
}

ALLOWED_HOSTS = []

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)
