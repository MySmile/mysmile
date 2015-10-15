from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

from django.conf import settings

from apps.api.v2.serializers import ContactSerializer, LangsSerializer, ContentSerializer
from apps.preferences.models import Preferences
from apps.pages.models import Page, Page_translation


class ContactView(APIView):
    def get(self, request, format=None):
        serializer = ContactSerializer()
        content = {'data': serializer.data, 'code': status.HTTP_200_OK}
        return Response(content)

class LangsView(APIView):
    def get(self, request, format=None):
        serializer = LangsSerializer()
        content = {'data': serializer.data, 'code': status.HTTP_200_OK}
        return Response(content)

class ContentView(APIView):

    # def dispatch(self, request, *args, **kwargs):
    #     if not settings.MYSMILE_REST_API:
    #         # raise PermissionDenied('Forbidden')
    #         print('MYSMILE_REST_API == ', settings.MYSMILE_REST_API)
    #     return super(ContentView, self).dispatch(request, *args, **kwargs)

    def get(self, request, format=None):
        """
        @TODO in-progress
        """
        # if not settings.MYSMILE_REST_API:
        #     raise PermissionDenied('Forbidden')

        lang = request.GET.get('lang', 'en')
        slug = request.GET.get('slug', None)


        content = Page_translation.objects.filter(lang=lang,
                                                  page__status=Page.STATUS_PUBLISHED,
                                                  page__ptype__in=[Page.PTYPE_API,
                                                                   Page.PTYPE_MENU_API]
                                                  ).order_by('page__sortorder')


        serializer = ContentSerializer(content, many=True)
        # print('serializer -----get_initial------- ', serializer.get_initial())
        content = {'data': serializer.data, 'code': status.HTTP_200_OK}
        return Response(content)

