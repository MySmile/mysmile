from django.conf.urls import patterns, include, url, handler404
from django.http import HttpResponse
from django.conf import settings
from django.contrib.staticfiles.views import serve as serve_static
from django.views.decorators.cache import never_cache

# comment the next two lines to disable the admin:
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

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # comment the next line to disable the admin:
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


