from django.conf.urls import patterns, url

from apps.admin.update.views import CheckUpdate


urlpatterns = patterns('',
    url(r'^admin/check-update/', CheckUpdate.as_view(url='/admin/')),
    )

