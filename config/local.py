# secret settings
import os
from mysmile.settings.base import BASE_DIR


DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR_PATCH_SETTINGS = False

SECRET_KEY = '=)1+x0_f%6t&$4gftv-^^w20kr)+1ut8js0@0(gt6cx8z6kxlc'

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

ADMINS = (
    ('admin', 'info@mysmile.com.ua'),
)
