"""
Django settings/local.py for MySmile development project.
"""
import os
import datetime

from .base import *
from config.local import *


TEMPLATE_DEBUG = DEBUG

# apps
THIRD_PARTY_APPS = ()

# Apps specific for this project go here.
LOCAL_APPS = (
    'apps.api',
    'apps.pages',
    'apps.sitemap',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION

MEDIA_ROOT = os.path.join(BASE_DIR, '..',  'media/')
STATIC_ROOT = os.path.join(BASE_DIR, '..', '')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'static/'),
    os.path.join(BASE_DIR,  '..', 'media/'),
)

TEMPLATE_DIRS = (
     os.path.join(BASE_DIR, '..', 'templates'),
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}
