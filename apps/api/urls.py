from django.conf.urls import patterns, url
from apps.api.views import MySmileApi
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',
    url(r'^(?P<resource>[a-z]+)$', csrf_exempt(MySmileApi.as_view())),
)


