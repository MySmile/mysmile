from django.conf.urls import url, patterns, include

urlpatterns = patterns('',
    url(r'', include('apps.api.v1.urls', namespace='default')),
    # url(r'^v2/', include('apps.api.v2.urls', namespace='v2')),
)

