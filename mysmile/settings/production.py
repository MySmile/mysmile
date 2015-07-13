"""
Django settings/production.py for MySmile deploy project.
"""
from .base import *
from config.production import *
from config.mysmile import *


APP_MIDDLEWARE_CLASSES = (
    'apps.utils.middlewares.ExceptionLoggingMiddleware',
    'apps.utils.middlewares.AdminLocaleOneLangMiddleware',
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
    'apps.update',
    'apps.utils',
    )

# another apps
THIRD_PARTY_APPS = ('debug_toolbar',
                    'compressor',
                    )

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'mysmile_cache_table',
    }
}

CACHE_MIDDLEWARE_SECONDS = 60*60 #60*60*24

# compressor settings
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',  'compressor.filters.cssmin.CSSMinFilter']

# production only
# python3 manage.py check --deploy
#SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
#SECURE_SSL_REDIRECT = True
#SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
