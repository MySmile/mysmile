# secret settings
import os
from mysmile.settings.base import BASE_DIR


DEBUG = False

SECRET_KEY = '=)1+x0_f%6t&$4gftv-^^w20kr)+1ut8js0@0(gt6cx8z6kxlc'

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


ALLOWED_HOSTS = [''] # like mysmile.com.ua

ADMINS = (
    ('admin', 'AdminEmail@email.com'),
)


"""
* Empty '' string means some app_setting "off"
* For PHONE: http://en.wikipedia.org/wiki/Telephone_numbering_plan 
* Go to the http://www.google.com/analytics/ to get the GOOGLE_ANALITYCS_CODE
* For inner_type page only <= MAX_INNERLINK_HISTORY
"""

app_settings = {
    'PHONE': '000 000 000 00 00', 
    'EMAIL': 'myemail@email.com',
    'SKYPE': 'myskype',
    'GOOGLE_ANALITYCS_CODE': '',
    'MAX_INNERLINK_HISTORY': 4, 
    'REST_API': True
}





