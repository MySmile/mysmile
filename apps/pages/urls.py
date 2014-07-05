from django.conf.urls import patterns, url

from apps.pages.views import MySmilePage, MySmilePageRedirectView


urlpatterns = patterns('',
    url(r'^$', MySmilePageRedirectView.as_view(), name='home'),
    url(r'^(?P<lang>[a-z]{2})/$', MySmilePageRedirectView.as_view(), name='page'),
    url(r'^(?P<lang>[a-z]{2})/(?P<slug>[a-z,A-Z,-]+)\.html$', MySmilePage.as_view(), name='page'),
)






