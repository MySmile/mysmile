from django import http

from pages.managers import PagesManager
from mysmile.settings import LANGUAGES


def ls_check(view_func):
    """Validation lang and slug parameters.
    Use before call view function
    """
    def _wrapped_view_func(request, *args, **kwargs):
        if (('lang' not in kwargs) or ('slug' not in kwargs)):
            w = PagesManager()
            entry_point = w.get_first_slug()
            # automatic language selection
            if 'HTTP_ACCEPT_LANGUAGE' in request.META:
                for k in LANGUAGES:
                    if k[0] in request.META['HTTP_ACCEPT_LANGUAGE']:
                        lang = k[0]
                        k = 0
                    else:
                        lang = LANGUAGES[0][0]
            else:
                lang = LANGUAGES[0][0]
            return http.HttpResponseRedirect(user_settings['DOMAIN_NAME'] +
                                             lang + '/' + entry_point + '.html')
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view_func
