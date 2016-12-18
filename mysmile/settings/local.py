"""
Django settings/local.py for MySmile development project.
"""
from .base import *
from config.local import *
from config.mysmile import *


APP_MIDDLEWARE_CLASSES = (
    'apps.api.middlewares.VersionSwitchMiddleware',
    'apps.utils.middlewares.ExceptionLoggingMiddleware',
    'apps.utils.middlewares.AdminLocaleOneLangMiddleware',
)

THIRD_PARTY_MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

MIDDLEWARE_CLASSES = DJANGO_MIDDLEWARE_CLASSES + \
                     APP_MIDDLEWARE_CLASSES + \
                     THIRD_PARTY_MIDDLEWARE_CLASSES

# Apps specific for this project go here.
LOCAL_APPS = (
    'apps.api',
    'apps.pages',
    'apps.preferences',
    'apps.sitemap',
    'apps.admin.update',
    'apps.admin.fail_login',
    'apps.utils',
    )

# another apps
THIRD_PARTY_APPS = ('debug_toolbar',
                    'compressor',
                    'rest_framework',
                    )

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'mysmile_cache_table',
        # 'TIMEOUT': None,
    }
}

CACHE_MIDDLEWARE_SECONDS = 5 #60*60*24

# compressor settings
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',  'compressor.filters.cssmin.CSSMinFilter']


if MYSMILE_ADMIN_FAIL_LOGIN_ENABLE:
    AUTHENTICATION_BACKENDS = ('apps.admin.fail_login.backends.FailLoginModelBackend',)
else:
    AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
