from django.db import connections, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from apps.preferences.models import Preferences
from apps.pages.models import Page, Page_translation

@receiver(post_save) # instead of @receiver(post_save, sender=Rebel)
def clear_cache(sender, instance=None, created=False, **kwargs):
    list_of_models = ('Page', 'Page_translation', 'Preferences')
    if sender.__name__ in list_of_models: # this is the dynamic part you want
        cursor = connections['default'].cursor()
        cache_table = settings.CACHES['default']['LOCATION']
        cursor.execute(' '.join(['DELETE FROM ', cache_table]))
        transaction.commit_unless_managed(using='default')




