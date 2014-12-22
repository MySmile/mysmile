"""
Django settings/local.py for MySmile development project.
"""
import os
import shutil
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
    # os.path.join(STATIC_ROOT, 'admin/'),
    # os.path.join(STATIC_ROOT, 'fonts/'),
    # os.path.join(STATIC_ROOT, 'media/'),
    os.path.join(STATIC_ROOT, 'third-party-components/'),
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': tempfile.mkdtemp(dir=os.path.join(STATIC_ROOT, 'tmp/')),
        'TIMEOUT': None,
    }
}

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = False
CACHE_MIDDLEWARE_SECONDS = 60*60*24
CACHE_MIDDLEWARE_KEY_PREFIX = 'mysmile'

# flush tmp dir after restart server
path_to_cache = os.path.join(STATIC_ROOT, 'tmp/')
for item in os.listdir(path_to_cache):
    shutil.rmtree(os.path.join(path_to_cache, item), ignore_errors=True)