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
from mysmile.user_settings import user_settings  # import user settings PHONE, EMAIL, etc.
from pages.managers import PagesManager  #all connection to db
from pages.decorators import ls_check

logger = logging.getLogger(__name__)  # Get an instance of a logger

@ls_check
def page(request, lang='', slug=''): #, c={}):
    w = PagesManager()
    c = w.get_content(lang, slug)
    c['nav'] = w.get_nav(lang)
    c['menu_flag'] = w.get_menu_flags(slug)
    c['inav'] = w.get_inner_nav(request, c['menu'], slug)
    c['logo_link'] = '/'+lang+'/'+w.get_first_slug()+'.html'
    c['lang'] = lang
    c['slug'] = slug
    
    c.update(user_settings)
    c['current_year'] = datetime.datetime.now().strftime('%Y')
      
    t = get_template('pages/page.html')
    html = t.render(Context(c))
    return HttpResponse(html)
  

