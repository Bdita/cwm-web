from .base import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

# once frontend is deployed
ALLOWED_HOSTS = [".herokuapp.com"]

# what to do with production database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}


CORS_ORIGIN_WHITELIST = (
    'https://coffeewithbandita.herokuapp.com',
)
