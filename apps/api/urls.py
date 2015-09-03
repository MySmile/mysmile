from django.conf.urls import *

urlpatterns = patterns('',
    #url(r'', include('apps.api.v2.urls', namespace='default')),
    url(r'^v1/', include('apps.api.v1.urls', namespace='v1')),
)