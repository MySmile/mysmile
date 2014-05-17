import os, PIL
from PIL import Image, ImageDraw, ImageFont

from django import template
register = template.Library()

from mysmile.settings.main import STATIC_ROOT, BASE_DIR, DEBUG
 

@register.filter(name='email2img')
def email2img(email):
    """ protect email via img
    """
    try:
        os.path.isfile(STATIC_ROOT+'static/images/email2img.png')
        if DEBUG:
            email_mod_time = round(os.stat(BASE_DIR+'config/local.py').st_mtime)
        else:
            email_mod_time = round(os.stat(BASE_DIR+'config/production.py').st_mtime)
            
        email2img_mod_time = round(os.stat(STATIC_ROOT+'static/images/email2img.png').st_mtime)
        if email_mod_time > email2img_mod_time:
            raise IOError
        else:
            return """<img src="/static/images/email2img.png" alt="email">"""
    
    except (OSError, IOError):
        color_mode="RGBA"
        background_color=(0,0,0,0) # full transparent
        fontfile = STATIC_ROOT+'static/fonts/TimesNewRomanCE.ttf'
        fontsize = 16

        try:
            font = ImageFont.truetype(fontfile, fontsize)
            width, height = font.getsize(email)
            # add fontsize%10 for fix some visual bug
            im = Image.new(color_mode, (width, height+fontsize%10), background_color)
            draw  =  ImageDraw.Draw(im)
            draw.text((0,0), email, (0,0,0), font=font)
            img_full_path = STATIC_ROOT+'static/images/email2img.png'
            im.save(img_full_path)
        except Exception:
            # return non-protected email. In future: log this error!
            return '<a href="mailto:'+email+'">'+email+'</a>'
        else:
            return """<img src="/static/images/email2img.png" alt="email" />"""


