"""
Django settings/local.py for MySmile development project.
"""
import os
import tempfile

from .base import *
from config.local import *


# apps
THIRD_PARTY_APPS = ()

# Apps specific for this project go here.
LOCAL_APPS = (
    'apps.api',
    'apps.pages',
    'apps.preferences',
    'apps.sitemap',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = (
    os.path.join(STATIC_ROOT, 'themes/default/'),
    os.path.join(STATIC_ROOT, 'media/'),
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': tempfile.mkdtemp(dir=os.path.join(STATIC_ROOT, 'tmp/')),
        'TIMEOUT': None,
    }
}
