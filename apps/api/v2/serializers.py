import pytz

from django.conf import settings

from rest_framework import serializers

from apps.preferences.models import Preferences
from apps.pages.models import Page, Page_translation

class DateTimeTzSerializer(serializers.Serializer):
    def to_native(self, value):
        localize = pytz.timezone(settings.TIME_ZONE).localize(value)
        return str(localize)

class ContactSerializer(serializers.Serializer):
    data =  Preferences.objects.get_contact()

class LangsSerializer(serializers.Serializer):
    data = [item[0] for item in settings.LANGUAGES]

class ContentSerializer(serializers.Serializer):
    menu = serializers.CharField()

#class ContentSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Page_translation
#        fields = ('menu', 'name', 'col_central')


    # content = Page_translation.objects.filter(lang=lang, page__status=Page.STATUS_PUBLISHED, page__ptype__in=[Page.PTYPE_API, Page.PTYPE_MENU_API]).order_by('page__sortorder').values_list('page__slug', 'menu')
    # data = [{item[0]: item[1]} for item in content]


