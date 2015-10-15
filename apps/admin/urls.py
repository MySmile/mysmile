from django.conf.urls import url, patterns, include

urlpatterns = patterns('',
    url(r'', include('apps.admin.update.urls',)),
)
