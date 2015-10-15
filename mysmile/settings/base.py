# -*- coding: utf-8 -*-
"""
Django settings/base.py for MySmile project.
"""
import os, sys
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..')


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
    'django.middleware.common.BrokenLinkEmailsMiddleware',
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

USE_I18N = True

USE_L10N = True

USE_TZ = True
TIME_ZONE = 'UTC'

LANGUAGES = (
    ('uk', 'Українська'),
    ('en', 'English'),
#    ('pl', 'Polski'),
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
            os.path.join(BASE_DIR, 'mysmile/templates'),
            os.path.join(BASE_DIR, 'apps/pages/templates/themes'),
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

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning'
}

LOGGING = {
    'version': 1,
    # True if the default configuration is completely overridden
    'disable_existing_loggers': False,
    'formatters': {
         'verbose': {
             'format' :
                 '%(asctime)s: %(name)s, line %(lineno)d: '
                 '%(levelname)s: %(message)s ',
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
               'level': 'DEBUG',
               'class': 'logging.handlers.RotatingFileHandler',
               'formatter': 'verbose',
               'filename': os.path.join(BASE_DIR,  'log/'+datetime.datetime.now().strftime('%Y-%m-%d')+'.log'),
               'maxBytes': 1024*1024*5, # 5Mb
               'backupCount': 5
           },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'null': {
            "class": 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null', ],
        },
        'django.db.backends': {
            'handlers': ['null', ],
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['null', ],
        },
        '': {
            'handlers': ['console', 'file'],
            'level': "DEBUG",
        },

    },
}

USE_ETAGS = True

LOCALE_PATHS = (os.path.join(BASE_DIR, 'mysmile/locale/'),
                )
