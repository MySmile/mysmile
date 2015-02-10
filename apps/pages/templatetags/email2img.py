import os
from PIL import Image, ImageDraw, ImageFont
import logging
logger = logging.getLogger(__name__)

from django.conf import settings
from django import template
register = template.Library()


@register.filter(name='email2img')
def email2img(email):
    """ protect email via img on production server, if DEBUG = False
    """
    if settings.DEBUG:
        logger.error("DEBUG = True, e-mail is not protected from spambots!")
        return '<a href="mailto:' + email + '">' + email + '</a>'
    else:
        try:
            email2img_mod_time = round(os.stat(os.path.join(settings.STATIC_ROOT, 'images/email2img.png')).st_mtime)
            email_mod_time = round(os.stat(os.path.join(settings.BASE_DIR, '/../../config/production.py')).st_mtime)
            if email_mod_time > email2img_mod_time:
                raise IOError  # force update email2img.png

        except (OSError, IOError):
            color_mode = "RGBA"
            background_color = (0, 0, 0, 0)  # full transparent
            fontfile = settings.STATIC_ROOT + 'fonts/TimesNewRomanCE.ttf'
            fontsize = 16
            try:
                font = ImageFont.truetype(fontfile, fontsize)
                width, height = font.getsize(email)
                # add fontsize%10 for fix some visual bug
                im = Image.new(color_mode, (width, height + fontsize % 10), background_color)
                draw = ImageDraw.Draw(im)
                draw.text((0, 0), email, (0, 0, 0), font=font)
                img_full_path = settings.STATIC_ROOT + 'images/email2img.png'
                im.save(img_full_path)
            except Exception:
                logger.error("Error creating image file from email. Wrong path to the font or target email2img.png?")
                return '<a href="mailto:' + email + '">' + email + '</a>'
            else:
                return """<img src="/static/images/email2img.png" alt="email" />"""
        else:
            return """<img src="/static/images/email2img.png" alt="email" />"""
