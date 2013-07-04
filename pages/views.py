# import user settings PHONE, EMAIL, etc. 
# import user settings PHONE, EMAIL, etc. 
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.http import HttpResponse,  HttpRequest
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django import http
import datetime

from pages.models import Page, Page_translation
from mysmile import user_settings


def page(request,lang='',slug=''):
	#built all menu&links
	if lang in user_settings.ALL_LANGS:
		cursor = connection.cursor()
		cursor.execute('SELECT P.slug, PT.menu FROM Page P, Page_translation PT WHERE \
			P.id = PT.page_id and P.status = 1 and  PT.lang = %s ORDER BY P.sortorder',[lang])
		nav = cursor.fetchall()
		
		cursor.execute('SELECT PT.lang FROM Page P, Page_translation PT WHERE \
			P.id = PT.page_id and P.status = 1 and P.slug = %s',[slug])
		menu_flag = cursor.fetchall()
	else:
		return HttpResponse("Unknown lang! Valid ",user_settings.ALL_LANGS," only.")
	
	c = {}
	c['nav'] = nav
	c['menu_flag'] = list(list(i)[0] for i in menu_flag)# some magic
	c['lang'] = lang
	c['slug'] = slug

	from_page = get_object_or_404(Page, slug=c['slug'],status=1)
	p = get_object_or_404(Page_translation, lang=c['lang'],page_id=from_page.id)

	#get user settings
	c['ALL_LANGS']=user_settings.ALL_LANGS
	if user_settings.PHONE:
		c['PHONE'] = user_settings.PHONE
	if user_settings.EMAIL:
		c['EMAIL'] = user_settings.EMAIL
    #defence the email: convert it to myemail.png!
	#pass	
		
	if user_settings.SKYPE:
		c['SKYPE'] = user_settings.SKYPE
	if user_settings.GOOGLE_ANALITYCS_CODE:
		c['GOOGLE_ANALITYCS_CODE']=user_settings.GOOGLE_ANALITYCS_CODE
	
	c['STATIC_URL'] = settings.STATIC_URL
	c['MEDIA_URL'] = settings.MEDIA_URL

	c['photo'] = from_page.photo
	c['color'] = from_page.color
	
	c['meta_title'] = p.meta_title
	c['meta_description'] = p.meta_description
	c['meta_keywords'] = p.meta_keywords
	c['photo_alt'] = p.photo_alt

	#get content
	c['name'] = p.name
	c['central_col'] = p.central_col
	c['right_col'] = p.right_col
	
	c['bottom_cols'] = []
	if ( p.bottom_col1 ):
		c['bottom_cols'].append(p.bottom_col1)
	if ( p.bottom_col2 ):
		c['bottom_cols'].append(p.bottom_col2)
	if ( p.bottom_col3 ):
		c['bottom_cols'].append(p.bottom_col3)
		
	c['current_year']=datetime.datetime.now().strftime('%Y')
	
	t = get_template('pages/page.html')
	html=t.render(Context(c))

	return HttpResponse(html)

def home(request,lang='',slug=''):
    if ( (''==slug) or (''==lang) ):
        entry_point= Page.objects.raw('SELECT id,slug FROM Page ORDER BY sortorder ASC')[0]
        #detect locale from browser
        if 'HTTP_ACCEPT_LANGUAGE' in request.META:
            for k in user_settings.ALL_LANGS:
                if k in request.META['HTTP_ACCEPT_LANGUAGE']:
                    lang=k
                    k=0
                else:
                    lang = user_settings.ALL_LANGS[0] 
        else:
            lang = user_settings.ALL_LANGS[0]
        return http.HttpResponseRedirect(user_settings.DOMAIN_NAME+\
               lang+'/'+entry_point.slug+'.html')
    else:
        return HttpResponse('Some unknown error! :(')
