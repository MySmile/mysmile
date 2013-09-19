from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.http import HttpResponse,  HttpRequest
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django import http
import datetime
import logging  # import the logging library

from pages.models import Page, Page_translation
from mysmile import user_settings  # import user settings PHONE, EMAIL, etc.
from pages.managers import PagesManager  #all connection to db
from pages.decorators import ls_check

logger = logging.getLogger(__name__)  # Get an instance of a logger

@ls_check
def page(request, lang='', slug='',c={}):
    w = PagesManager()
    nav = w.get_nav(lang)
    menu_flag = w.get_menu_flags(slug)
    c = w.get_content(lang, slug)
    inav = w.get_inner_nav(request, c['menu'], slug)
    c['logo_link'] = '/'+lang+'/'+w.get_first_slug()+'.html'
    c['lang'] = lang
    c['slug'] = slug
    c['nav'] = nav
    c['inav'] = inav
    c['menu_flag'] = menu_flag
    c['ALL_LANGS'] = user_settings.ALL_LANGS  # get user settings
    if user_settings.PHONE:
        c['PHONE'] = user_settings.PHONE
    if user_settings.EMAIL:
        c['EMAIL'] = user_settings.EMAIL
    if user_settings.SKYPE:
        c['SKYPE'] = user_settings.SKYPE
    if user_settings.GOOGLE_ANALITYCS_CODE:
        c['GOOGLE_ANALITYCS_CODE'] = user_settings.GOOGLE_ANALITYCS_CODE
    
    c['STATIC_URL'] = settings.STATIC_URL
    c['MEDIA_URL'] = settings.MEDIA_URL
    c['current_year'] = datetime.datetime.now().strftime('%Y')

    t = get_template('pages/page.html')
    html = t.render(Context(c))
    return HttpResponse(html)
  
#~ paste somewhere this code!
#~ if lang not in user_settings.ALL_LANGS:
    #~ logger.error('Unsupported language parameter: '+lang)
    #~ return HttpResponse("Impossible to load current page. Unsupported language parameter. \
            #~ Please use one of supported", user_settings.ALL_LANGS, ".")
 #~ 
