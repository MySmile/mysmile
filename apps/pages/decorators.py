#from django import http
#from django.http import Http404

#from apps.pages.managers import PagesManager
#from mysmile.settings.main import LANGUAGES


#def ls_check(view_func):
    #"""Validation lang and slug parameters.
    #Use before call view function
    #"""
    #def _wrapped_view_func(request, *args, **kwargs):
        #if (('lang' not in kwargs) or ('slug' not in kwargs)):
            #w = PagesManager()
            #first_slug = w.get_first_slug()
            #if first_slug == None:
                #raise Http404
            ## adaptive language selection
            #if 'HTTP_ACCEPT_LANGUAGE' in request.META:
                #for k in LANGUAGES:
                    #if k[0] in request.META['HTTP_ACCEPT_LANGUAGE']:
                        #lang = k[0]
                        #k = 0
                    #else:
                        #lang = LANGUAGES[0][0]
            #else:
                #lang = LANGUAGES[0][0]
            #return http.HttpResponseRedirect('/' + lang + '/' + first_slug + '.html')
        #else:
            #return view_func(request, *args, **kwargs)
    #return _wrapped_view_func
#