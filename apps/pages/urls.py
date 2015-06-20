from django.conf.urls import patterns, url

from apps.pages.views import PageView, PageRedirectView


urlpatterns = patterns('',
    url(r'^$', PageRedirectView.as_view(), name='home'),
    url(r'^(?P<lang>[a-z]{2})/$', PageRedirectView.as_view(), name='page'),
    url(r'^(?P<lang>[a-z]{2})/(?P<slug>[a-zA-Z0-9-]+)\.html$', PageView.as_view(), name='page'),
    )
