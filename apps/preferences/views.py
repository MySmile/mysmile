from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template import RequestContext, loader, Template, TemplateDoesNotExist
from django.views.decorators.csrf import requires_csrf_token

import logging
logger = logging.getLogger(__name__)  # Get an instance of a logger

from apps.pages.models import Page, Page_translation


@requires_csrf_token
def e404(request, template_name='404.html'):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        template = Template(
            '<h1>Not Found</h1>'
            '<p>The requested URL {{ request_path }} was not found on this server.</p>')
    try:
        slug = request.path.split('/')[-1].split('.html')[0]  # get slug from path request
        #  Verify the existence of the slug
        slug = Page.objects.filter(slug=slug,
                                   status=Page.STATUS_PUBLISHED,
                                   ptype__in=[Page.PTYPE_MENU, Page.PTYPE_MENU_API, Page.PTYPE_INNER]).values_list('slug', flat=True)[0]
    except IndexError as err:
        slug = None
        logger.error(str(err))

    langs = Page_translation.objects.filter(page__slug=slug).values_list('lang', flat=True) if slug else ''
    return HttpResponseNotFound(template.render(RequestContext(request, {'request_host': request.get_host, 'request_path': request.path, 'slug': slug, 'langs': langs})))


@requires_csrf_token
def e500(request, template_name='500.html'):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        template = Template(
            '<h1>Not Found</h1>'
            '<p>The requested URL {{ request_path }} was not found on this server.</p>')
    return HttpResponseNotFound(template.render(RequestContext(request, {'request_path': request.path, })))

# like  e403
def csrf_failure(request, reason=""):
    template_name = '403.html'
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        template = Template(
            '<b>HTTP Forbidden</b>'
            '<p>The requested URL {{ request_path }} forbidden.</p>')
    logger.error('error 403: ' + str(request))
    return HttpResponseNotFound(template.render(RequestContext(request, {'request_path': request.path, })))


