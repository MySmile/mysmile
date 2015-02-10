# -*- coding: utf-8 -*-
"""
Django settings/base.py for MySmile project.
"""
import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

DJANGO_MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

    
ROOT_URLCONF = 'mysmile.urls'

WSGI_APPLICATION = 'mysmile.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    #~ ('pl', 'Polski'),
    ('uk', 'Українська'),
    ('ru', 'Русский'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'static/themes/default'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, #the default configuration is completely overridden
    'formatters': {
         'verbose': {
             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
             'datefmt' : "%d/%b/%Y %H:%M:%S"
         },
         'simple': {
             'format': '%(levelname)s %(message)s'
         },
     },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },

    },
    'handlers': {
        'file_info': {
               'level': 'INFO',
               'class': 'logging.handlers.RotatingFileHandler',
               'formatter': 'verbose',
               'filters': ['require_debug_true'],
               'filename': os.path.join(BASE_DIR,  '../log/'+datetime.datetime.now().strftime('%Y-%m-%d')+'_INFO.log'),
               'maxBytes': 1024*1024*5, # 5 MB
               'backupCount': 5
           },
        'file_error': {
               'level': 'ERROR',
               'class': 'logging.handlers.RotatingFileHandler',
               'formatter': 'verbose',
               'filters': ['require_debug_true'],
               'filename': os.path.join(BASE_DIR,  '../log/'+datetime.datetime.now().strftime('%Y-%m-%d')+'_ERROR.log'),
               'maxBytes': 1024*1024*5, # 5 MB
               'backupCount': 5
           },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        }
    },

    'loggers': {
        '': {
            'handlers': ['file_info', 'file_error'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

CSRF_FAILURE_VIEW = 'apps.preferences.views.csrf_failure'

