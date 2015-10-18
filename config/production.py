# secret production settings
import os
from mysmile.settings.base import BASE_DIR

DEBUG = False

COMPRESS_ENABLED = True

DEBUG_TOOLBAR_PATCH_SETTINGS = DEBUG

SECRET_KEY = ''

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

# for example: ALLOWED_HOSTS = ['mysite.com']
ALLOWED_HOSTS = ['demo.mysmile.com.ua']

# Enter path to media folder on server.
MEDIA_ROOT = ''

# Enter path to static folder on server.
STATIC_ROOT = ''

COMPRESS_ROOT = STATIC_ROOT


ADMINS = (
    ('admin', 'support@mysmile.com.ua'),
)

MANAGERS = (
    ('admin', 'support@mysmile.com.ua'),
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = 'mail@mysite.com'
DEFAULT_FROM_EMAIL = SERVER_EMAIL
EMAIL_SUBJECT_PREFIX = 'something like [MYSITE]'
EMAIL_HOST = 'adress of IMAP server'
EMAIL_HOST_USER = 'mail@mysite.com'
EMAIL_HOST_PASSWORD = 'password to email'

EMAIL_USE_SSL = True
EMAIL_PORT = 465
# or
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587

# This is only used if CommonMiddleware is installed
PREPEND_WWW = False

# This is only used if CommonMiddleware is installed
APPEND_SLASH = True

# To fix the django.fcgi url problem
FORCE_SCRIPT_NAME = ''
