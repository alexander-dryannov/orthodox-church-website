from .base import *
from os import getenv

load_dotenv(find_dotenv('.env_local'))

DEBUG = True

SECRET_KEY = getenv('SECRET_KEY')

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
