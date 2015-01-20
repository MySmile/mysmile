# secret settings
import os
from mysmile.settings.base import BASE_DIR


DEBUG = False
TEMPLATE_DEBUG = DEBUG
#DEBUG_TOOLBAR_PATCH_SETTINGS = False

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

# like ['demomysmile.com.ua', 'www.demo.mysmile.com.ua']
ALLOWED_HOSTS = ['demo.mysmile.com.ua', 'www.demo.mysmile.com.ua']

ADMINS = (
    ('admin', 'AdminEmail@email.com'),
)
