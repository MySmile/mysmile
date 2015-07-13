# -*- coding: utf-8 -*-
"""
Django settings/base.py for MySmile project.
"""
import os, sys
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
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
    ('ua', 'Українська'),
    ('ru', 'Русский'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

CSRF_FAILURE_VIEW = 'apps.preferences.views.csrf_failure'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, '../apps/pages/templates/themes'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here
                'apps.utils.context_processors.mysmile_version',
                'apps.utils.context_processors.mysmile_theme',
                # or use this list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',

                # 'django.template.context_processors.debug',
                # 'django.template.context_processors.request',
                # 'django.contrib.auth.context_processors.auth',
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

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
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
        'file': {
               'level': 'DEBUG',
               'class': 'logging.handlers.RotatingFileHandler',
               'formatter': 'verbose',
               'filters': ['require_debug_true'],
               'filename': os.path.join(BASE_DIR,  '../log/'+datetime.datetime.now().strftime('%Y-%m-%d')+'.log'),
               'maxBytes': 1024*1024*5, # 5 MB
               'backupCount': 5
           },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_true']
        }
    },

    'loggers': {
        '': {
            'handlers': ['file',],
            # 'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },


    },
}
