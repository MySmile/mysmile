from django.http import HttpResponseNotFound
from django.template import RequestContext, loader, Template, TemplateDoesNotExist
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic.base import RedirectView, TemplateView
from django.conf import settings
from django.core.cache import cache
from django.core import signing

import logging
logger = logging.getLogger(__name__)  # Get an instance of a logger

from apps.pages.models import Page
from apps.preferences.models import Preferences


class PageRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'page'

    def get_redirect_url(self, *args, **kwargs):
        # get first slug
        slug = Page.objects.filter(status=Page.STATUS_PUBLISHED, ptype__in=[Page.PTYPE_MENU, Page.PTYPE_MENU_API]).values_list('slug', flat=True).order_by('sortorder').first()
        try:
            lang = kwargs['lang']
        except KeyError:  # adaptive language selection
            lang = settings.LANGUAGES[0][0]
            if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
                for k in settings.LANGUAGES:
                    if k[0] in self.request.META['HTTP_ACCEPT_LANGUAGE']:
                        lang = k[0]
                        k = 0  # break cycle "for"
        return super(PageRedirectView, self).get_redirect_url(lang=lang, slug=slug)


class PageView(TemplateView):

    def get_template_names(self):
        return settings.MYSMILE_THEME + '/page.html'

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        c = Page.objects.get_content(kwargs['lang'], kwargs['slug'])
        c.update(Preferences.objects.get_all())
        c['inav'] = self.get_additional_dynamic_menu(self.request, kwargs['slug'], c['menu'], c['page__ptype'], int(c['MAX_INNERLINK_HISTORY']))

        c['MYSMILE_THEME'] = settings.MYSMILE_THEME
        context.update(c)
        return context

    def get_additional_dynamic_menu(self, request, slug, menu, ptype, max_innerlink_history):
        inner_nav = request.session.get('inner_nav', [])
        if ptype == Page.PTYPE_INNER:
            if not [slug, menu] in inner_nav:  # work with sessions
                inner_nav.append([slug, menu]) # add to dynamic menu
                request.session['inner_nav'] = inner_nav  # save data to the session
                while len(inner_nav) > max_innerlink_history:
                    inner_nav.pop(0)
        return inner_nav


