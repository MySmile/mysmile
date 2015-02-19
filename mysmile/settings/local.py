"""
Django settings/local.py for MySmile development project.
"""
import os
import shutil
import tempfile

from .base import *
from config.local import *


APP_MIDDLEWARE_CLASSES = (
    'apps.utils.middlewares.ExceptionLoggingMiddleware',
)

THIRD_PARTY_MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

MIDDLEWARE_CLASSES = DJANGO_MIDDLEWARE_CLASSES + APP_MIDDLEWARE_CLASSES + THIRD_PARTY_MIDDLEWARE_CLASSES


# Apps specific for this project go here.
LOCAL_APPS = (
    'apps.api',
    'apps.pages',
    'apps.preferences',
    'apps.sitemap',
    'apps.utils',
    )

# another apps
THIRD_PARTY_APPS = ('debug_toolbar',
                    'compressor',
                    )

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),

    os.path.join(BASE_DIR, 'static/themes/default/'),
    os.path.join(BASE_DIR, 'static/fonts/'),
    os.path.join(BASE_DIR, 'static/third-party-components/'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'mysmile_cache_table',
    }
}

#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = False
CACHE_MIDDLEWARE_SECONDS = 60*60*24
#CACHE_MIDDLEWARE_KEY_PREFIX = 'mysmile'

# compressor settings
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_ROOT = os.path.join(BASE_DIR, 'static/')

COMPRESS_ENABLED = True

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',  'compressor.filters.cssmin.CSSMinFilter']