from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt

from apps.api.v1.views import MySmileApi


urlpatterns = [
    url(r'(?P<resource>[a-z,0-9]+)$', csrf_exempt(MySmileApi.as_view())),
]

urlpatterns = format_suffix_patterns(urlpatterns)

