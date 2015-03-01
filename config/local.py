# secret settings
import os
from mysmile.settings.base import BASE_DIR
from config.mysmile import *

DEBUG = True

COMPRESS_ENABLED = True

DEBUG_TOOLBAR_PATCH_SETTINGS = False

SECRET_KEY = '=)1+x0_f%6t&$4gftv-^^w20kr)+1ut8js0@0(gt6cx8z6kxlc'

TEMPLATE_DEBUG = DEBUG

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/mysmile.sqlite3'),
        # 'USER': '',
        # 'PASSWORD': '',
        # 'HOST': '',
        # 'PORT': '',
    }
}


ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Enter path to static folder in server.
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

COMPRESS_ROOT = STATIC_ROOT

CACHE_MIDDLEWARE_SECONDS = 60*60*24


ADMINS = (
    ('admin', 'info@mysmile.com.ua'),
)
