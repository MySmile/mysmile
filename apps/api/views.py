#~ from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponse, HttpResponseNotFound
from django.utils.datastructures import MultiValueDictKeyError
#~ from django.views.generic import View
from django.views.generic.base import View

from django.db import DatabaseError
from django.core.exceptions import FieldError

from apps.pages.models import Page, Page_translation
from mysmile.user_settings import user_settings
from mysmile.settings import LANGUAGES



class MySmileApi(View):

    def get(self, request, resource):
        if resource == 'content':
            try:
                self.lang = request.GET['lang']
            except MultiValueDictKeyError:
                self.lang = 'en'
            try:
                self.slug = self.request.GET['slug']
            except MultiValueDictKeyError:
                self.slug = ''
            response_data = self.response_data(self.lang, self.slug)
        else:
            response_data = self.response_data_short(resource)

        return HttpResponse(json.dumps(response_data), mimetype="application/json", status = response_data['code'] )
    
    def response_data(self, lang, slug):
        response_data = {}
        response_data['code'] = 200
        
        if slug == '':             
            response_data['data'] = list(Page_translation.objects.filter(lang=self.lang, page__status=1).values_list('name', flat=True))
                        
        elif slug == 'contact':
            response_data['data'] = {'email':user_settings['EMAIL'],
                                'phone':user_settings['PHONE'],
                                'skype':user_settings['SKYPE']
                                }            
        
        elif slug == 'language':
            response_data['data'] = [item[0] for item in LANGUAGES]

        else:
            try:
                page_id = Page.objects.filter(slug=slug, status=1).values('id')
                if page_id:
                    content = Page_translation.objects.filter(lang=lang, page__status=1, page_id=page_id).values('page__color', 'page__photo', 'menu', 'name', 'col_central', 'col_right', 'youtube', 'col_bottom_1', 'col_bottom_2', 'col_bottom_3', 'photo_alt', 'photo_description', 'meta_title', 'meta_description', 'meta_keywords')
                    if content: #  if lang exists
                        response_data['data'] = list(content)
                    else:
                        response_data['code'] = 404
                        response_data['msg'] = 'Not Found'
                else:
                    response_data['code'] = 404
                    response_data['msg'] = 'Not Found'
            except (DatabaseError, FieldError):
                response_data['code'] = 500
                response_data['msg'] = 'Internal Server Error'

        return response_data

    def response_data_short(self, resource):
        response_data = {}
        response_data['code'] = 200

        if resource == 'contact':
            try:
                response_data['data'] = {'email':user_settings['EMAIL'],
                                        'phone':user_settings['PHONE'],
                                        'skype':user_settings['SKYPE']
                                        }
            except KeyError:
                response_data['code'] = 500
                response_data['msg'] = 'Internal Server Error'                            

        elif resource == 'language':
            try:
                response_data['data'] = [item[0] for item in LANGUAGES]
            except KeyError:
                response_data['code'] = 500
                response_data['msg'] = 'Internal Server Error'          
        else:
            response_data['code'] = 500
            response_data['msg'] = 'Internal Server Error'
        return response_data


    def post(self, request):
        response_data = {}
        response_data['code'] = 502
        response_data['msg'] = 'Method Not Allowed'
        return HttpResponse(json.dumps(response_data), mimetype="application/json", status=502)


#~ class BadRequest(Exception):
    #~ def __init__(self, code):
        #~ self.response_data = {}
        #~ self.response_data['code'] = 500
        #~ self.response_data['msg'] = 'Internal Server Error'




