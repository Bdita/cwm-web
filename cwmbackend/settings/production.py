from .base import *

DEBUG = False

SECRET_KEY = config('SECRET_KEY')

# once frontend is deployed
# ALLOWED_HOSTS = []

# what to do with production database
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
