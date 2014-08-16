from django.http import HttpResponseNotFound 
from django.template import RequestContext, loader, Template, TemplateDoesNotExist
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic.base import RedirectView, TemplateView
#logger = logging.getLogger(__name__)  # Get an instance of a logger

from mysmile.settings.main import LANGUAGES
from apps.pages.managers import PagesManager
from apps.pages.models import Page, Page_translation


class MySmilePageRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'page'

    def get_redirect_url(self, *args, **kwargs):
        # get first slug
        slug = Page.objects.filter(status=Page.STATUS_PUBLISHED, ptype__in=[Page.PTYPE_MENU,Page.PTYPE_MENU_API]).values_list('slug', flat=True).order_by('sortorder').first()
        try:
            lang = kwargs['lang']
        except KeyError: # adaptive language selection
            lang = LANGUAGES[0][0]
            if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
                for k in LANGUAGES:
                    if k[0] in self.request.META['HTTP_ACCEPT_LANGUAGE']:
                        lang = k[0]
                        k = 0 # break cycle "for"          
        return super(MySmilePageRedirectView, self).get_redirect_url(lang=lang, slug=slug)


class MySmilePageView(TemplateView):
    template_name = ''
    def get_context_data(self, **kwargs):
        context = super(MySmilePageView, self).get_context_data(**kwargs)
        w = PagesManager()
        context.update(w.get_content(self.request, kwargs['lang'], kwargs['slug']))
        return context


@requires_csrf_token
def my_custom_404_view(request, template_name='404.html'):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        template = Template(
            '<h1>Not Found</h1>'
            '<p>The requested URL {{ request_path }} was not found on this server.</p>')
    try:
        slug = request.path.split('/')[-1].split('.html')[0]  # get slug from path request
        slug = Page.objects.filter(slug=slug, status=Page.STATUS_PUBLISHED, ptype__in=[Page.PTYPE_MENU,Page.PTYPE_MENU_API]).values_list('slug', flat=True)[0]
    except IndexError:
        pass
    #  Verify the existence of the slug
    
    langs = Page_translation.objects.filter(page__slug=slug).values_list('lang', flat=True) if slug else ''
    return HttpResponseNotFound(template.render(RequestContext(request, {'request_host': request.get_host, 'request_path': request.path, 'slug': slug, 'langs': langs})))

@requires_csrf_token
def my_custom_500_view(request, template_name='500.html'):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        template = Template(
            '<h1>Not Found</h1>'
            '<p>The requested URL {{ request_path }} was not found on this server.</p>')
    return HttpResponseNotFound(template.render(RequestContext(request, {'request_path': request.path,})))
