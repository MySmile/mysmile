from django.conf.urls import patterns, url
from django.http import HttpResponse
from django.conf import settings

urlpatterns = patterns('',
    url(r'^Sitemap\.xml$', 'apps.sitemap.views.SitemapXML'),

    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nHost: " + \
                                              settings.ALLOWED_HOSTS[0] +
                                              "\nSitemap: http://" + settings.ALLOWED_HOSTS[0] + \
                                              "/Sitemap.xml", content_type="text/plain")),
    #(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
)
