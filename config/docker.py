# secret local settings
import os
from mysmile.settings.base import BASE_DIR

DEBUG = True

COMPRESS_ENABLED = False

DEBUG_TOOLBAR_PATCH_SETTINGS = False

SECRET_KEY = '=)1+x0_f%6t&$4gftv-^^w20kr)+1ut8js0@0(gt6cx8z6kxlc'

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

# uncomment for use MySql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mysmile',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'mysmile.dev']

# Enter path to media folder
MEDIA_ROOT = os.path.join(BASE_DIR, 'mysmile/media/')

# Enter path to static folder
STATIC_ROOT = os.path.join(BASE_DIR, 'mysmile/static/')

COMPRESS_ROOT = STATIC_ROOT

ADMINS = (
    ('admin', 'info@mysmile.com.ua'),
)


