# secret settings
import os
from mysmile.settings.base import BASE_DIR


DEBUG = True

SECRET_KEY = '=(j+x0_f%2t&$4gftv-^^w2mkr)+2ut8js0@0(gp6cx8z7kxlb'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db/mysmile.sqlite3'),
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


#~ from django.conf import settings


#~ from apps.pages.settings import *

#~ from apps.pages.models import Settings

#~ settings.APP_SETTINGS = Settings.objects.filter(key__in = ['KEY_PHONE', 'KEY_EMAIL', 'KEY_SKYPE', 'KEY_GOOGLE_ANALITYCS_CODE']).values('key','value')


#~ try:
    #~ 
#~ app_settings = {
 #~ 'PHONE': '000 000 000 00 00',
 #~ 'EMAIL': 'myemail@email.com',
 #~ 'SKYPE': 'myskype',
 #~ 'GOOGLE_ANALITYCS_CODE': '',
 #~ 'MAX_INNERLINK_HISTORY': 4,
 #~ 'REST_API': True
#~ }
