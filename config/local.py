# secret settings
import os
from mysmile.settings.base import BASE_DIR


DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = '=(j+x0_f%2t&$4gftv-^^w2mkr)+2ut8js0@0(gp6cx8z7kxlb'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/mysmile.sqlite3'),
        #~ 'USER': '',
        #~ 'PASSWORD': '',
        #~ 'HOST': '',
        #~ 'PORT': '',
    }
}


ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

ADMINS = (
    ('admin', 'info@mysmile.com.ua'),
)
