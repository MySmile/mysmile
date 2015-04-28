import os
from PIL import Image, ImageDraw, ImageFont

from django.db import connections, transaction
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from django.contrib.admin.models import LogEntry

from apps.pages.models import Page
from apps.preferences.models import Preferences

import logging
logger = logging.getLogger(__name__)


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


@receiver(post_save)
def email2img(sender, instance, created, **kwargs):
    """ protect email via image
    """
    if created and not isinstance(sender, LogEntry):
        email = Preferences.objects.filter(key='EMAIL').values_list('value', flat=True)
        if email:
            color_mode = "RGBA"
            background_color = (0, 0, 0, 0)  # full transparent
            fontfile = os.path.join(settings.STATIC_ROOT, 'fonts/TimesNewRomanCE.ttf')
            fontsize = 16
            textcolor = (119 , 119, 119)
            try:
                font = ImageFont.truetype(fontfile, fontsize)
                width, height = font.getsize(email)
                # add fontsize%10 for fix some visual bug
                im = Image.new(color_mode, (width, height + fontsize % 10), background_color)
                draw = ImageDraw.Draw(im)
                draw.text((0, 0), email[0], textcolor, font=font)
                img_full_path = settings.STATIC_ROOT + 'themes/default/images/email2img.png'
                im.save(img_full_path)
            except Exception as err:
                logger.error(str(err))

pre_delete.connect(clear_photo_file, sender=Page, dispatch_uid="clear_photo_file")
post_save.connect(email2img, sender=Preferences, dispatch_uid="email2img")


