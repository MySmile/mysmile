import os

from django.db import connections, transaction
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings

from apps.pages.models import Page

@receiver(post_save)
def clear_cache(sender, instance=None, created=False, **kwargs):
    list_of_models = ('Page', 'Page_translation', 'Preferences')
    if sender.__name__ in list_of_models:
        cursor = connections['default'].cursor()
        cache_table = settings.CACHES['default']['LOCATION']
        cursor.execute(' '.join(['DELETE FROM ', cache_table]))
        transaction.commit_unless_managed(using='default')


def clear_photo_file(sender, instance, **kwargs):
    file = getattr(instance, 'photo')
    if file and os.path.exists(file.path):
        os.remove(file.path)

pre_delete.connect(clear_photo_file, sender=Page, dispatch_uid="clear_photo_file")

