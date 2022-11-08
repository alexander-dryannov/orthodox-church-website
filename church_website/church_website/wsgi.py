"""
WSGI config for church_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv(find_dotenv(Path(__file__).resolve().parent.joinpath('settings/.env')))

if bool(int(os.getenv('PRODUCTION', None))):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church_website.settings.pro')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church_website.settings.local')

application = get_wsgi_application()
