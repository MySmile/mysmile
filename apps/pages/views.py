from django import http
from django.template import RequestContext, loader, Template, TemplateDoesNotExist
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render_to_response
#import logging

from apps.pages.managers import PagesManager
from apps.pages.decorators import ls_check

#logger = logging.getLogger(__name__)  # Get an instance of a logger


@ls_check
def page(request, lang='', slug=''):
    w = PagesManager()
    c = w.get_content(request, lang, slug)
    return render_to_response('page.html',
                               c, context_instance=RequestContext(request))

@requires_csrf_token
def my_custom_404_view(request, template_name='404.html'):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        template = Template(
            '<h1>Not Found</h1>'
            '<p>The requested URL {{ request_path }} was not found on this server.</p>')
    return http.HttpResponseNotFound(template.render(RequestContext(request, {'request_path': request.path})))

