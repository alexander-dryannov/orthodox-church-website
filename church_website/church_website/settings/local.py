from .base import *
from os import getenv

load_dotenv(find_dotenv('.env_local'))

DEBUG = True

SECRET_KEY = 'RPtE"<^s{IJ]~a0-LSe$__nDIih}G25*kI>y@h!9Jr^uo*P|vT'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
