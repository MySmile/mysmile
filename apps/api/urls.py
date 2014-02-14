from django.conf.urls import patterns, url


urlpatterns = patterns('apps.api.views',
    url(r'^content$', 'get_content'),
    url(r'^contact$', 'get_contact'),
    url(r'^languages$', 'get_languages'),
    
       #~ url(r'^api/content?slug=(?P<resource>[a-z,_]+)&v=1&lang=(?P<lang>[a-z]{2})&format=json$', 'get_content'),  
)

