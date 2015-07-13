"""aaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import patterns, include, url, handler404
from django.http import HttpResponse
from django.conf import settings
from django.contrib.staticfiles.views import serve as serve_static
from django.views.decorators.cache import never_cache
from django.contrib import admin


urlpatterns = patterns('',
    url('', include('apps.pages.urls')),
    url(r'^api/', include('apps.api.urls')),

    url('', include('apps.sitemap.urls')),
    #(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nHost: " + \
                                              settings.ALLOWED_HOSTS[0] +
                                              "\nSitemap: http://" + settings.ALLOWED_HOSTS[0] + \
                                              "/Sitemap.xml", content_type="text/plain")),

    url('', include('apps.update.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
)


handler404 = 'apps.preferences.views.e404'
handler500 = 'apps.preferences.views.e500'


if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', never_cache(serve_static)),
    )

if settings.DEBUG_TOOLBAR_PATCH_SETTINGS:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )


