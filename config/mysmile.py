# MySmile settings
from apps.preferences.models import Preferences

MYSMILE_VERSION = '0.7.2'

try:
    MYSMILE_THEME = Preferences.objects.filter(key='THEME').values_list('value', flat=True)[0]
except Exception as err:
    MYSMILE_THEME = 'modern'

try:
    MYSMILE_REST_API = 'True' in Preferences.objects.filter(key='REST_API').values_list('value', flat=True)
except Exception as err:
    MYSMILE_REST_API = False

# Fail login settings
MYSMILE_ADMIN_FAIL_LOGIN_ENABLE = True
MYSMILE_ADMIN_FAIL_LOGIN_ATTEMPTS = 5
MYSMILE_ADMIN_FAIL_LOGIN_TIMEOUT = 15 # minutes
