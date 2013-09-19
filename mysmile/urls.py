from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import handler404
from django.contrib import sitemaps
from django.shortcuts import render
from django.http import HttpResponse

from mysmile import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^$', 'pages.views.page'),
    #~ (r'^$', 'pages.views.home'),
    (r'^(?P<lang>[a-z]{2})/$', 'pages.views.page'),
    #~ (r'^(?P<lang>[a-z]{2})/$', 'pages.views.home'),

    (r'^(?P<lang>[a-z]{2})/(?P<slug>[a-z,A-Z,-]+)\.html$', 'pages.views.page'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nHost: demo.mysmile.com.ua\nSitemap: \
  http://demo.mysmile.com.ua/Sitemap.xml", mimetype="text/plain")),

   	(r'^Sitemap\.xml$', 'sitemap.views.SitemapXML'),
)


handler404 = 'mysmile.views.my_custom_404_view'


if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )


