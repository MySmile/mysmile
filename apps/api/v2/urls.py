from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from apps.api.v2.views import ContactView, LangsView, ContentView


urlpatterns = [
    url(r'contact/$', ContactView.as_view()),
    url(r'language/$', LangsView.as_view()),
    url(r'content', ContentView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)