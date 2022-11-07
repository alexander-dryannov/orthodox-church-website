from .base import *
from os import getenv

DEBUG = False

SECRET_KEY = getenv('SECRET_KEY')

ALLOWED_HOSTS = ['your_domain']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('NAME'),
        'USER': getenv('USER'),
        'PASSWORD': getenv('PASSWORD'),
        'HOST': getenv('HOST'),
        'PORT': int(getenv('PORT'))
    }
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

admin_username = getenv('EMAIL_USERNAME')
admin_email = getenv('EMAIL_HOST_USER')

ADMINS = (
    (admin_username, admin_email),
)

if getenv('EMAIL_USE_TLS') is not None:
    EMAIL_USE_TLS = bool(int(getenv('EMAIL_USE_TLS')))
if getenv('EMAIL_USE_SSL') is not None:
    EMAIL_USE_SSL = bool(int(getenv('EMAIL_USE_SSL')))
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_PORT = int(getenv('EMAIL_PORT'))
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
SERVER_EMAIL = getenv('SERVER_EMAIL')
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')
