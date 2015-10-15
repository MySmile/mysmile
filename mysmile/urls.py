from django.conf.urls import patterns, include, url, handler404
from django.conf import settings
from django.contrib.staticfiles.views import serve as serve_static
from django.views.decorators.cache import never_cache
from django.contrib import admin


urlpatterns = patterns('',
    url('', include('apps.pages.urls')),
    url(r'^api/', include('apps.api.urls')),

    url('', include('apps.sitemap.urls')),

    url('', include('apps.admin.urls')),
    url(r'^api/', include('apps.api.urls', namespace='api')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
)


handler404 = 'apps.preferences.views.e404'
handler500 = 'apps.preferences.views.e500'

admin.site.site_header = 'MySmile administration'

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', never_cache(serve_static)),
    )

    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )



