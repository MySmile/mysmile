from django.db import models, IntegrityError
from django.core.cache import cache
from django.core import signing

from apps.settings.models import Settings


class SettingsManager(models.Manager):
    """Send all settings into cache with key = app_settings
    """    
    def __init__(self):
        if not cache.get('app_settings'):
            try:
                data = Settings.objects.all().values('key', 'value')
                app_settings = {}
                for item in data:
                    app_settings.update({item['key']: item['value']})
                cache.set('app_settings', signing.dumps(app_settings))
                ee = signing.loads(cache.get('app_settings'))
            except IntegrityError:
                pass

    def get(self, key):
        """ Generic get anyone setting by Setting key. Return {'key': value}.
        """
        try:
            some_setting = {key: signing.loads(cache.get('app_settings'))[key]}
        except KeyError:
            some_setting = {}
        return some_setting

    def get_contact(self):
        contact = {}
        for key, value in Settings.CONTACT.items():
            contact.update({value: self.value(key)})
        return contact

    def value(self, key):
        """ Generic get value setting by Setting key. Return value.
        """
        try:
            value = signing.loads(cache.get('app_settings'))[key]
        except KeyError:
            value = None
        return value
