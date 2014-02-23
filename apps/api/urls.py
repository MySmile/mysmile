from django.conf.urls import patterns, url
from apps.api.views import MySmileApi


urlpatterns = patterns('',
    url(r'^(?P<resource>[a-z]+)$', MySmileApi.as_view()),
)


