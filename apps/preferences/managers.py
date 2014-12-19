import shutil
import os
from django.db import models, IntegrityError
from django.core.cache import cache
from django.core import signing
from django.conf import settings

from apps.preferences.models import Preferences


class PreferencesManager(models.Manager):
    """Send all settings into cache with key = app_settings
    """    
    def __init__(self):
        if not cache.get('app_settings'): 
            # flush tmp dir
            path_to_cache = os.path.join(settings.STATIC_ROOT, 'tmp/')
            for item in os.listdir(path_to_cache):
                shutil.rmtree(os.path.join(path_to_cache, item), ignore_errors=True) 
            try:
                data = Preferences.objects.all().values('key', 'value')
                app_settings = {}
                for item in data:
                    app_settings.update({item['key']: item['value']})
                cache.set('app_settings', signing.dumps(app_settings))
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
        for key, value in Preferences.CONTACT.items():
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
