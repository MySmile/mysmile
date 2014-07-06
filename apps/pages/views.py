import http
from django.template import RequestContext, loader, Template, TemplateDoesNotExist
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render_to_response
from django.views.generic import View
from django.views.generic.base import RedirectView
#logger = logging.getLogger(__name__)  # Get an instance of a logger

from mysmile.settings.main import LANGUAGES
from apps.pages.managers import PagesManager
from apps.pages.models import Page


class MySmilePageRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'page'

    def get_redirect_url(self, *args, **kwargs):
        # get first slug
        slug = Page.objects.filter(status=1, ptype=1).values_list('slug', flat=True).order_by('sortorder').first()
        try:
            lang = kwargs['lang']
        except KeyError:
            lang = LANGUAGES[0][0]
        return super(MySmilePageRedirectView, self).get_redirect_url(lang=lang, slug=slug)


class MySmilePage(View):

    def get(self, request, *args, **kwargs):
        w = PagesManager()
        c = w.get_content(request, kwargs['lang'], kwargs['slug'])
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