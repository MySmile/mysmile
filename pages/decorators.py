from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django import http
from django.http import HttpResponse

from pages.managers import PagesManager
from mysmile.user_settings import user_settings

def ls_check(view_func):
    """Validation lang and slug parameters.
    Use before call view function
    """
    def _wrapped_view_func(request, *args, **kwargs):
        if (('lang' not in kwargs) or ('slug' not in kwargs)):
            w = PagesManager()
            entry_point = w.get_first_slug()
            if 'HTTP_ACCEPT_LANGUAGE' in request.META:  # automatic language selection
                for k in user_settings['ALL_LANGS']:
                    if k in request.META['HTTP_ACCEPT_LANGUAGE']:
                        lang = k
                        k = 0
                    else:
                        lang = user_settings['ALL_LANGS'][0] 
            else:
                lang = user_settings['ALL_LANGS'][0]
            return http.HttpResponseRedirect(user_settings['DOMAIN_NAME']+\
                   lang+'/'+entry_point+'.html')
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view_func
