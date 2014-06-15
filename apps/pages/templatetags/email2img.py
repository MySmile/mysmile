import os, PIL
from PIL import Image, ImageDraw, ImageFont
import logging
logger = logging.getLogger(__name__) 

from django import template
register = template.Library()
from mysmile.settings.main import STATIC_ROOT, BASE_DIR, DEBUG
from apps.pages.exceptions import MySmilePagesException
 
 
@register.filter(name='email2img')
def email2img(email):
    """ protect email via img on production server, if DEBUG = False
    """
    try:
        if DEBUG: # DEBUG = False on production!
            raise MySmilePagesException('E-mail is not protected from spambots!', 100)
            
        email_mod_time = round(os.stat(BASE_DIR+'config/production.py').st_mtime)
        email2img_mod_time = round(os.stat(STATIC_ROOT+'static/images/email2img.png').st_mtime)
        
        if email_mod_time > email2img_mod_time: # update file email2img.png
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

    except MySmilePagesException, e:
        logger.warning("E-mail is not protected from spambots!")
        return '<a href="mailto:'+email+'">'+email+'</a>'

    else:
        return """<img src="/static/images/email2img.png" alt="email" />"""


