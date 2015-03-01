from django.db import connections, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save)
def clear_cache(sender, instance=None, created=False, **kwargs):
    list_of_models = ('Page', 'Page_translation', 'Preferences')
    if sender.__name__ in list_of_models:
        cursor = connections['default'].cursor()
        cache_table = settings.CACHES['default']['LOCATION']
        cursor.execute(' '.join(['DELETE FROM ', cache_table]))
        transaction.commit_unless_managed(using='default')
