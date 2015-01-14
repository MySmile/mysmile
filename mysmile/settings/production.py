"""
Django settings/production.py for MySmile deploy project.
"""
import os
import shutil
import tempfile

from .base import *
from config.production import *


APP_MIDDLEWARE_CLASSES = (
    'apps.preferences.middlewares.ExceptionLoggingMiddleware',
)

THIRD_PARTY_MIDDLEWARE_CLASSES = (
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

MIDDLEWARE_CLASSES = DJANGO_MIDDLEWARE_CLASSES + APP_MIDDLEWARE_CLASSES + 
THIRD_PARTY_MIDDLEWARE_CLASSES

# Apps specific for this project go here.
LOCAL_APPS = (
    'apps.api',
    'apps.pages',
    'apps.preferences',
    'apps.sitemap',
)

# another apps
THIRD_PARTY_APPS = (#'debug_toolbar',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Enter path to static folder in server.
# For example, STATIC_ROOT = '/home/you_server_account/domains/you_domain_name/public_html/static/'
STATIC_ROOT = ''


# prepare tmp dir for cache
if not os.path.exists(os.path.join(STATIC_ROOT, 'tmp/')):
    os.makedirs(os.path.join(STATIC_ROOT, 'tmp/'))

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': tempfile.mkdtemp(dir=os.path.join(BASE_DIR, '..', 'tmp/')),
        'TIMEOUT': None,
    }
}
