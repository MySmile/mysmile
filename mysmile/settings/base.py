# -*- coding: utf-8 -*-
"""
Django settings/base.py for MySmile project.
"""
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#~ BASE_DIR = os.path.realpath(os.path.dirname(__file__))
BASE_DIR =  os.path.dirname(os.path.realpath(__file__))

#~ SITE_ID = 1

########## APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #~ 'django.contrib.sites',
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



"""
* Empty '' string means some app_setting "off"
* Put 'DOMAIN': '' for 127.0.0.1 and registered 'domain.com' for production
* For PHONE: http://en.wikipedia.org/wiki/Telephone_numbering_plan 
* Go to the http://www.google.com/analytics/ to get the GOOGLE_ANALITYCS_CODE
* For inner_type page only <= MAX_INNERLINK_HISTORY
"""

app_settings = {
    'PHONE': '000 000 000 00 00', 
    'EMAIL': 'myemail@email.com',
    'SKYPE': 'myskype',
    'DOMAIN': '', # put '' for localhost 127.0.0.1
    'GOOGLE_ANALITYCS_CODE': '',
    'MAX_INNERLINK_HISTORY': 4, 
    'REST_API': False
}


