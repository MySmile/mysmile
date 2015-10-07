# secret local settings
import os
from mysmile.settings.base import BASE_DIR

DEBUG = True

COMPRESS_ENABLED = False

DEBUG_TOOLBAR_PATCH_SETTINGS = True

SECRET_KEY = '=)1+x0_f%6t&$4gftv-^^w20kr)+1ut8js0@0(gt6cx8z6kxlc'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'mysmile/db/mysmile.sqlite3'),
        # 'USER': '',
        # 'PASSWORD': '',
        # 'HOST': '',
        # 'PORT': '',
    }
}

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Enter path to media folder
MEDIA_ROOT = os.path.join(BASE_DIR, 'mysmile/media/')

# Enter path to static folder
STATIC_ROOT = os.path.join(BASE_DIR, 'mysmile/static/')

COMPRESS_ROOT = STATIC_ROOT

ADMINS = (
    ('admin', 'info@mysmile.com.ua'),
)


