#~ from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponse, HttpResponseNotFound
from django.utils.datastructures import MultiValueDictKeyError


from apps.pages.models import Page, Page_translation
from mysmile.user_settings import user_settings
from mysmile.settings import LANGUAGES


def get_content(request):
    try:
        lang = request.GET['lang']
    except MultiValueDictKeyError:
        lang = 'en'
        
    try:
        slug = request.GET['slug']
    except MultiValueDictKeyError:
        slug = ''
        
    if slug == 'contact':
        response_data = {}
        response_data['msg'] = 200
        response_data['data'] = {'email':user_settings['EMAIL'],
                            'phone':user_settings['PHONE'],
                            'skype':user_settings['SKYPE']
                            }
        return HttpResponse(json.dumps(response_data), mimetype="application/json")
        
    elif slug == 'language':
        response_data = {}
        response_data['msg'] = 200
        response_data['data'] = [item[0] for item in LANGUAGES]
        return HttpResponse(json.dumps(response_data), mimetype="application/json")
    
    elif slug=='':        
        response_data = {}
        response_data['msg'] = 200
        response_data['data'] = list(Page_translation.objects.filter(lang=lang, page__status=1).values_list('name', flat=True))
        return HttpResponse(json.dumps(response_data), mimetype="application/json")
    
    else:        
        response_data = {}
        page_id = Page.objects.filter(slug=slug, status=1).values('id')
        if page_id:
            content = Page_translation.objects.filter(lang=lang, page__status=1, page_id=page_id).values('page__color', 'page__photo', 'menu', 'name', 'col_central', 'col_right', 'youtube', 'col_bottom_1', 'col_bottom_2', 'col_bottom_3', 'photo_alt', 'meta_title', 'meta_description', 'meta_keywords')
            response_data['data'] = list(content)
            response_data['msg'] = 200
        else:
            response_data['code'] = 404
            response_data['msg'] = 'Not Found'

        
        #~ response_data = dict('data', content)
        return HttpResponse(json.dumps(response_data), mimetype="application/json")





class ApiException(Exception):
    pass
    



#~ def get_languages(request):
    #~ response_data = {}
    #~ response_data['msg'] = 200
    #~ response_data['data'] = [item[0] for item in LANGUAGES]
    #~ return HttpResponse(json.dumps(response_data), mimetype="application/json")




#~ def get_contact(request):
    #~ response_data = {}
    #~ response_data['msg'] = 200
    #~ response_data['data'] = {'email':user_settings['EMAIL'],
                            #~ 'phone':user_settings['PHONE'],
                            #~ 'skype':user_settings['SKYPE']
                            #~ }
    #~ return HttpResponse(json.dumps(response_data), mimetype="application/json")

#~ def get_content(request, resource, lang):
    #~ resource = request.GET['resource']
    #~ lang = request.GET['lang']
    #~ 
    #~ print('AAA---->> ', resource, ' bbbb --- ', lang)
    #~ response_data = {}
    #~ response_data['msg'] = 200
    #~ response_data['data'] = {'email':user_settings['EMAIL'],
                            #~ 'phone':user_settings['PHONE'],
                            #~ 'skype':user_settings['SKYPE']
                            #~ }
    #~ return HttpResponse(json.dumps(response_data), mimetype="application/json")
