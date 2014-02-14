#~ from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponse

from apps.pages.models import Page
from mysmile.user_settings import user_settings
from mysmile.settings import LANGUAGES

def get_contact(request):
    response_data = {}
    response_data['msg'] = 200
    response_data['data'] = {'email':user_settings['EMAIL'],
                            'phone':user_settings['PHONE'],
                            'skype':user_settings['SKYPE']
                            }
    return HttpResponse(json.dumps(response_data), mimetype="application/json")

def get_content(request):
    response_data = {}
    response_data['msg'] = 200
    response_data['data'] = list(Page.objects.filter(status=1).values_list('slug', flat=True))
    return HttpResponse(json.dumps(response_data), mimetype="application/json")

def get_languages(request):
    response_data = {}
    response_data['msg'] = 200
    response_data['data'] = [item[0] for item in LANGUAGES]
    return HttpResponse(json.dumps(response_data), mimetype="application/json")


