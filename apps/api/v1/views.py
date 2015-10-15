import json
from django.http import HttpResponse
from django.views.generic.base import View
from django.db import DatabaseError
from django.core.exceptions import FieldError
from django.conf import settings

from apps.pages.models import Page, Page_translation
from apps.api.v1.exceptions import MySmileApiException
from apps.preferences.models import Preferences


import logging
logger = logging.getLogger(__name__)


class MySmileApi(View):

    def dispatch(self, request, *args, **kwargs):
        api_on_off = Preferences.objects.filter(key='REST_API').values('value')
        if 'False' == api_on_off:
            raise MySmileApiException('Forbidden', 403)
        return super(MySmileApi, self).dispatch(request, *args, **kwargs)

    def get(self, request, resource):
        self.lang = request.GET.get('lang', 'en')
        self.slug = request.GET.get('slug', '')

        try:
            if resource == 'content':
                response_data = self.get_content(request)
            elif resource == 'language':
                response_data = self.get_language()
            elif resource == 'contact':
                response_data = self.get_contact()
            else:
                raise MySmileApiException('Not Found', 404)
        except IndexError:
            response_data = {'code': 404, 'msg': 'Not Found'}

        except MySmileApiException as inst:
            response_data = {'code': inst.code, 'msg': inst.msg}

        except (DatabaseError, FieldError, KeyError, Exception) as err:
            logger.error(err)
            # @FIXME: save exception details to log
            response_data = {'code': 500, 'msg': 'Internal Server Error'}

        return HttpResponse(json.dumps(response_data), content_type="application/json",
                            status=response_data['code'])

    def get_content(self, request):
        response_data = {'code': 200, 'data': {}}

        if self.slug == '':
            # get list of pages
            content = Page_translation.objects.filter(lang=self.lang, page__status=Page.STATUS_PUBLISHED, page__ptype__in=[Page.PTYPE_API, Page.PTYPE_MENU_API]).order_by('page__sortorder').values_list('page__slug', 'menu')

            if not content:
                raise MySmileApiException('Not Found', 404)
            response_data['data'] = [{item[0]: item[1]} for item in content]

            return response_data

        # get current page by slug
        page_id = Page.objects.filter(slug=self.slug, status=Page.STATUS_PUBLISHED, ptype__in=[Page.PTYPE_API, Page.PTYPE_MENU_API]).values('id')
        if not page_id:
            raise MySmileApiException('Not Found', 404)

        content = Page_translation.objects.filter(lang=self.lang, page__status=Page.STATUS_PUBLISHED, page_id=page_id, page__ptype__in=[Page.PTYPE_API, Page.PTYPE_MENU_API]).values(
            'page__color', 'page__photo', 'menu', 'name',
            'col_central', 'col_right', 'youtube', 'col_bottom_1',
            'col_bottom_2', 'col_bottom_3', 'photo_alt', 'photo_description',
            'meta_title', 'meta_description', 'meta_keywords')[0]

        if not content:
            raise MySmileApiException('Not Found', 404)

        response_data['data'] = {'menu': content['menu'],
                                 'name': content['name'],
                                 'col_central': content['col_central'],
                                 'col_right': content['col_right'],
                                 'youtube': content['youtube']
                                }

        response_data['data']['col_bottom'] = [content[item] for item in ['col_bottom_1', 'col_bottom_2', 'col_bottom_3'] if content[item]]

        response_data['data']['photo'] = {'src': request.build_absolute_uri('/static/' + content['page__photo']),
                                          'alt': content['photo_alt'],
                                          'description': content['photo_description']
                                          }

        return response_data

    def get_contact(self):
        response_data = {'code': 200}
        response_data['data'] = Preferences.objects.get_contact()
        return response_data

    def get_language(self):
        response_data = {'code': 200}
        response_data['data'] = [item[0] for item in settings.LANGUAGES]

        return response_data

    def post(self, request, resource):
        response_data = {'code': 502, 'msg': 'Method Not Allowed'}

        return HttpResponse(json.dumps(response_data), content_type="application/json", status=502)

    def put(self, request, resource):
        response_data = {'code': 502, 'msg': 'Method Not Allowed'}

        return HttpResponse(json.dumps(response_data), content_type="application/json", status=502)

    def delete(self, request, resource):
        response_data = {'code': 502, 'msg': 'Method Not Allowed'}

        return HttpResponse(json.dumps(response_data), content_type="application/json", status=502)
