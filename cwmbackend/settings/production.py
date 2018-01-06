from .base import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ["https://cwmbackend.herokuapp.com"]

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}


CORS_ORIGIN_WHITELIST = (
    'https://coffeewithbandita.herokuapp.com/booking',
)
