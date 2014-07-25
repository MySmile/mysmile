from django.db import models, IntegrityError
from django.core.cache import cache

from apps.settings.models import Settings


class SettingsManager(models.Manager):
    """Send all settings into cache with key = app_settings
    """
    def __init__(self):
        if not cache.get('app_settings'):
            try:
                data = Settings.objects.all().values('key','value')
            except IntegrityError:
                pass
            app_settings = {}
            for item in data:
                app_settings.update({item['key']:item['value']})
            cache.set('app_settings', app_settings)

    def get(self, key):
        """ Generic get anyone setting by Setting key. Return {'key': value}.
        """
        try:
            some_setting = {key: cache.get('app_settings')[key]}
        except KeyError:
            some_setting = {}
        return some_setting

    def get_contact(self):
        keys = ['PHONE', 'EMAIL', 'SKYPE']
        contact = {}
        for key in keys:
            contact.update(self.get(key))
        return contact

    def value(self, key):
        """ Generic get value setting by Setting key. Return value.
        """
        try:
            some_setting = cache.get('app_settings')[key]
        except KeyError:
            some_setting = None
        return some_setting


    #~ def get_google_analitycs_code(self):
        #~ temp = cache.get('app_settings')
        #~ print('temp = ', temp)
        #~ return {'GOOGLE_ANALITYCS_CODE': self.app_settings['GOOGLE_ANALITYCS_CODE']}
#~ 
    #~ def get_api_key(self):
        #~ return {'REST_API': self.app_settings['REST_API']}
#~ 
    #~ def get_max_innerlink_history(self):
        #~ return {'MAX_INNERLINK_HISTORY': self.app_settings['MAX_INNERLINK_HISTORY']}
#~ 
