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

logger = logging.getLogger(__name__)  # Get an instance of a logger


def page(request, lang='', slug='', c={}):
	if lang in user_settings.ALL_LANGS:
		w = PagesManager()
		nav = w.get_nav(lang)
		menu_flag = w.get_menu_flags(slug)
		cc = w.get_content(lang, slug)
		inav = w.get_inner_nav(request, cc['menu'], slug)
	else:
		logger.error('Unsupported language parameter: '+lang)
		return HttpResponse("Impossible to load current page. Unsupported language parameter. \
			Please use one of supported", user_settings.ALL_LANGS, ".")
	
	c['lang'] = lang
	c['slug'] = slug
	c['nav'] = nav
	c['inav'] = inav
	if cc['youtube']:
		cc['youtube'] = create_embed_url_youtube(cc['youtube'])
	c['menu_flag'] = menu_flag
	c.update(cc)

	c['bottom_cols'] = []  #  some processing of the columns...
	if c['bottom_col1']:
		c['bottom_cols'].append(c['bottom_col1'])
	if c['bottom_col2']:
		c['bottom_cols'].append(c['bottom_col2'])
	if c['bottom_col3']:
		c['bottom_cols'].append(c['bottom_col3'])

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
  
 
def home(request, lang='', slug=''):
	if (('' == slug) or ('' == lang)):
		w = PagesManager()
		entry_point = w.get_first_slug()
		if 'HTTP_ACCEPT_LANGUAGE' in request.META:  # automatic language selection
			for k in user_settings.ALL_LANGS:
				if k in request.META['HTTP_ACCEPT_LANGUAGE']:
					lang = k
					k = 0
				else:
					lang = user_settings.ALL_LANGS[0] 
		else:
			lang = user_settings.ALL_LANGS[0]
		return http.HttpResponseRedirect(user_settings.DOMAIN_NAME+\
			   lang+'/'+entry_point.slug+'.html')
	else:
		return HttpResponse('Application error. Please reload page or contact administrator.')


def create_embed_url_youtube(url):
	code = url.split('=')[-1]
	return 'https://www.youtube.com/embed/'+code+'?feature=player_detailpage'

# function get lang & slug from request
#~ def get_lang_slug(request):
	#~ url = HttpRequest.build_absolute_uri(request)
	#~ url = url.split('/')
	#~ temp = url[-1].split('.')
	#~ ls = {'slug':temp[0]}
	#~ ls['lang'] = url[-2] 
	#~ return ls
	
