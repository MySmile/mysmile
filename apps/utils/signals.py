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
        except (IndexError, Exception) as err:
            settings.MYSMILE_THEME = 'modern'
            logger.error(err)

        try:
            settings.MYSMILE_REST_API = 'True' in Preferences.objects.filter(key='REST_API').values_list('value', flat=True)
        except Exception as err:
            settings.MYSMILE_REST_API = False
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


def image_tuning(sender, instance, created=False, **kwargs):
    """ Implement preferences: IMAGE_QUALITY and IMAGE_AUTOSCALE
    """
    try:
        path = instance.photo.path
        if os.path.isfile(path):
            quality = int(Preferences.objects.filter(key='IMAGE_QUALITY').values_list('value', flat=True)[0])
            image = Image.open(path)
            image.save(path, quality=quality, optimize=True)

        autoscale = Preferences.objects.filter(key='IMAGE_AUTOSCALE').values_list('value', flat=True)[0]
        if os.path.isfile(path) and autoscale:
            image = Image.open(path)
            if image.width > 333: # 333px in right. TODO: create constan like MYSMILE_IMAGE_WIDTH = 333
                wpercent = (333/float(image.size[0]))
                hsize = int((float(image.size[1])*float(wpercent)))
                image = image.resize((333, hsize), PIL.Image.ANTIALIAS)
                image.save(path)
    except Exception as err:
        logger.error(err)

# group by sender
pre_delete.connect(clear_photo_file, sender=Page, dispatch_uid="clear_photo_file")
post_save.connect(image_tuning, sender=Page, dispatch_uid="image_tuning")

post_save.connect(email2img, sender=Preferences, dispatch_uid="email2img")
