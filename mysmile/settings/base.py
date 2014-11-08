# -*- coding: utf-8 -*-
"""
Django settings/base.py for MySmile project.
"""
import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR =  os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

########## APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'mysmile.urls'

WSGI_APPLICATION = 'mysmile.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

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
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, 'static/themes/default/'),
    os.path.join(BASE_DIR, 'media/'),
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'static/themes/default'),
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True, #the default configuration is completely overridden
    'formatters': {
         'verbose': {
             'format': '%(levelname)s %(asctime)s %(module)s.%(filename)s, line: %(lineno)d  \n%(pathname)s\n  %(message)s\n',
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
        'file': {
               'level': 'ERROR',
               'class': 'logging.FileHandler',
               'formatter': 'verbose',
               'filters': ['require_debug_true'],
               'filename': os.path.join(BASE_DIR,  '../log/ERRORS/'+datetime.datetime.now().strftime('%d-%m-%Y')+'_errors.log'),
           },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        }
    },

    'loggers': {
        'log2file': {
            'handlers': ['file'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
