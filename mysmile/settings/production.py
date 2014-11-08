"""
Django settings/local.py for MySmile development project.
"""
import os
import datetime
import tempfile

from .base import *
from config.production import *


# apps
THIRD_PARTY_APPS = ()

# Apps specific for this project go here.
LOCAL_APPS = (
    'apps.api',
    'apps.pages',
    'apps.settings',
    'apps.sitemap',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION

MEDIA_ROOT = os.path.join(BASE_DIR,  'media/')

# Enter path to static folder in server.
# For example, STATIC_ROOT = '/home/you_server_account/domains/you_domain_name/public_html/static/'
STATIC_ROOT = ''

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION':  tempfile.mkdtemp(dir=os.path.join(BASE_DIR, '..',  'tmp/')),

         #  in Django 1.7 You can set TIMEOUT to None so that, by default, cache keys never expire
        'TIMEOUT': 24*60*60*356*100,
    }
}
