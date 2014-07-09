from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^Sitemap\.xml$', 'apps.sitemap.views.SitemapXML'),
)
