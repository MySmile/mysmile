from django.template import RequestContext
from django.shortcuts import render_to_response
#import logging

from pages.managers import PagesManager
from pages.decorators import ls_check

#logger = logging.getLogger(__name__)  # Get an instance of a logger


@ls_check
def page(request, lang='', slug=''):
    w = PagesManager()
    c = w.get_content(request, lang, slug)
    return render_to_response('pages/page.html',
                               c, context_instance=RequestContext(request))
