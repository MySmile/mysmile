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
        cache_table = settings.CACHES['default']['LOCATION']
        try:
            with transaction.atomic():
                cursor = connections['default'].cursor()
                cursor.execute(' '.join(['DELETE FROM ', cache_table]))
        except Exception as err:
            logger.error(err)

    if sender.__name__=='Preferences':
        try:
            settings.MYSMILE_THEME = Preferences.objects.filter(key='THEME').values_list('value', flat=True)[0]

        except Exception as err:
            settings.MYSMILE_THEME = 'modern'
            logger.error(err)



def clear_photo_file(sender, instance, **kwargs):
    file = getattr(instance, 'photo')
    if file and os.path.exists(file.path):
        os.remove(file.path)


def email2img(sender, instance, created=False, **kwargs):
    """ protect email via image
    """

    if created == False and not isinstance(sender, LogEntry):
        email = Preferences.objects.filter(key='EMAIL').values_list('value', flat=True)
        if email:
            color_mode = "RGBA"
            background_color = (0, 0, 0, 0)  # full transparent
            fontfile = os.path.join(settings.STATIC_ROOT, 'fonts/TimesNewRomanCE.ttf')
            fontsize = 16
            textcolor = (119, 119, 119)
            try:
                font = ImageFont.truetype(fontfile, fontsize)
                width, height = font.getsize(email[0])
                # add fontsize%10 for fix some visual bug
                im = Image.new(color_mode, (width, height + fontsize % 10), background_color)
                draw = ImageDraw.Draw(im)
                draw.text((0, 0), email[0], textcolor, font=font)
                img_full_path = settings.STATIC_ROOT + 'themes/'+ \
                                settings.MYSMILE_THEME +'/images/email2img.png'
                im.save(img_full_path)
            except Exception as err:
                logger.error(err)





pre_delete.connect(clear_photo_file, sender=Page, dispatch_uid="clear_photo_file")
post_save.connect(email2img, sender=Preferences, dispatch_uid="email2img")
