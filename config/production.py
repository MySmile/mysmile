# secret production settings
import os
from mysmile.settings.base import BASE_DIR

DEBUG = False

COMPRESS_ENABLED = True

DEBUG_TOOLBAR_PATCH_SETTINGS = False

SECRET_KEY = ''

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

# for example: ALLOWED_HOSTS = ['mysite.com', 'www.mysite.com']
ALLOWED_HOSTS = ['demo.mysmile.com.ua', 'www.demo.mysmile.com.ua']

# Enter path to media folder on server.
MEDIA_ROOT = ''

# Enter path to static folder on server.
STATIC_ROOT = ''

COMPRESS_ROOT = STATIC_ROOT

ADMINS = (
    ('admin', 'info@mysmile.com.ua'),
)

# This is only used if CommonMiddleware is installed
PREPEND_WWW = False

# This is only used if CommonMiddleware is installed
APPEND_SLASH = True

# To fix the django.fcgi url problem
FORCE_SCRIPT_NAME = ''
