# MySmile settings
from django.conf import settings
from apps.preferences.models import Preferences

MYSMILE_VERSION = '0.7.1'

try:
    MYSMILE_THEME = Preferences.objects.filter(key='THEME').values_list('value', flat=True)[0]
except Exception as err:
    MYSMILE_THEME = 'modern'

try:
    MYSMILE_REST_API = 'True' in Preferences.objects.filter(key='REST_API').values_list('value', flat=True)
except Exception as err:
    MYSMILE_REST_API = False
