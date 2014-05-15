from django.conf.urls import patterns, include, url, handler404
from django.http import HttpResponse
from django.conf import settings
from django.contrib.staticfiles.views import serve as serve_static
from django.views.decorators.cache import never_cache

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from mysmile.settings.main import DEBUG, MEDIA_ROOT

urlpatterns = patterns('',

    (r'^$', 'apps.pages.views.page'),
    (r'^(?P<lang>[a-z]{2})/$', 'apps.pages.views.page'),
    (r'^(?P<lang>[a-z]{2})/(?P<slug>[a-z,A-Z,-]+)\.html$', 'apps.pages.views.page'),

    url(r'^api/', include('apps.api.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nHost: demo.mysmile.com.ua\nSitemap: \
  http://demo.mysmile.com.ua/Sitemap.xml", mimetype="text/plain")),

    (r'^Sitemap\.xml$', 'apps.sitemap.views.SitemapXML'),
)


handler404 = 'apps.pages.views.my_custom_404_view'


if DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', never_cache(serve_static)),
    )


