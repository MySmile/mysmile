from django.db import connections, transaction
from django.db.models.signals import post_save
from django.conf import settings

from apps.preferences.models import Preferences

# post_save signals for clear cache
def clear_cache(sender, instance, **kwargs):
    cursor = connections['default'].cursor()
    cache_table = settings.CACHES['default']['LOCATION']
    cursor.execute(' '.join(['DELETE FROM ', cache_table]))
    transaction.commit_unless_managed(using='default')

# register the signal
post_save.connect(clear_cache, sender=Preferences, dispatch_uid="clear_cache_after_changes")

