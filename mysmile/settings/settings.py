"""
Django settings/local.py for MySmile project.
"""
import os
import datetime
#~ from .base import *
#~ from config.local import *




#~ =================================


DEBUG = True

SECRET_KEY = '=(j+x0_f%2t&$4gftv-^^w2mkr)+2ut8js0@0(gp6cx8z7kxlb'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #~ 'NAME': os.path.join(BASE_DIR, 'db/mysmile.sqlite3'),
        'NAME': 'db/mysmile.sqlite3',
        #~ 'USER': '',
        #~ 'PASSWORD': '',
        #~ 'HOST': '', 
        #~ 'PORT': '', 
    }
}

ALLOWED_HOSTS = ['127.0.0.1']

ADMINS = (
    ('admin', 'info@mysmile.com.ua'),
)

"""
app settings
Empty '' string means setting "off"

http://en.wikipedia.org/wiki/Telephone_numbering_plan 

go to the http://www.google.com/analytics/ to get the GOOGLE_ANALITYCS_CODE

for inner_type page only <= MAX_INNERLINK_HISTORY
"""

app_settings = {
    'PHONE': '000 000 000 00 00', 
    'EMAIL': 'myemail@email.com',
    'SKYPE': 'myskype',
    'GOOGLE_ANALITYCS_CODE': '',
    'MAX_INNERLINK_HISTORY': 4, 
    'REST_API': False
}


#~ =================================



#~ ----------------------------------
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#~ BASE_DIR = os.path.realpath(os.path.dirname(__file__))
BASE_DIR =  os.path.dirname(os.path.realpath(__file__))


########## APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    #'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
    ('uk', 'Українська'),
    ('ru', 'Русский'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#~ MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = ('/media/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, 'media/'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

#~ -----------------------------


TEMPLATE_DEBUG = DEBUG

# apps
THIRD_PARTY_APPS = ()

# Apps specific for this project go here.
LOCAL_APPS = (
    #~ 'apps.api',
    #~ 'apps.pages',
    #~ 'apps.sitemap',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
#~ INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
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
