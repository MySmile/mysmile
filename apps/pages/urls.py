from django.conf.urls import patterns, url

from apps.pages.views import MySmilePageView, MySmilePageRedirectView


urlpatterns = patterns('',
    url(r'^$', MySmilePageRedirectView.as_view(), name='home'),
    url(r'^(?P<lang>[a-z]{2})/$', MySmilePageRedirectView.as_view(), name='page'),
    url(r'^(?P<lang>[a-z]{2})/(?P<slug>[a-z,A-Z,-]+)\.html$', MySmilePageView.as_view(template_name='page.html'), name='page'),
)
