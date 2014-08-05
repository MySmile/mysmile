from django.db import models
from django.core.cache import cache
from django.core import signing
from django.http import Http404

from mysmile.settings.main import LANGUAGES
from apps.pages.models import Page, Page_translation
from apps.settings.managers import SettingsManager


class PagesManager(SettingsManager):
            
    def get_content(self, request, lang=None, slug=None):
        c = self.get_page(lang, slug)
        c.update({'lang': lang, 'slug': slug})
        c['languages'] = LANGUAGES if len(LANGUAGES) > 1 else ''
        c.update(signing.loads(cache.get('app_settings')))

        c['main_menu'] = self.get_main_menu(lang)
        c['logo_slug'] = c['main_menu'][0]['page__slug']
        c['inav'] = self.get_additional_dynamic_menu(request, slug, c['menu'], c['page__ptype'], int(c['MAX_INNERLINK_HISTORY']))
        return c

    def get_main_menu(self, lang):
            main_menu = Page_translation.objects.filter(lang=lang, page__status=Page.STATUS_PUBLISHED, page__ptype__in=[Page.PTYPE_MENU,Page.PTYPE_MENU_API]).values('page__slug', 'menu').order_by('page__sortorder')
            return main_menu

    def get_additional_dynamic_menu(self, request, slug, menu, ptype, max_innerlink_history):
        inner_nav = request.session.get('inner_nav', [])
        if ptype == Page.PTYPE_INNER:
            if not [slug, menu] in inner_nav:  # work with sessions
                inner_nav.append([slug, menu]) # add to dynamic menu
                request.session['inner_nav'] = inner_nav  # save data to the session
                while len(inner_nav) > max_innerlink_history:
                    inner_nav.pop(0)
        return inner_nav

    def get_page(self, lang, slug):
        try:
            page = Page_translation.objects.filter(lang=lang, page__ptype__in = [Page.PTYPE_INNER,Page.PTYPE_MENU,Page.PTYPE_MENU_API], page__status=Page.STATUS_PUBLISHED, page__slug=slug).values('page__color', 'page__photo', 'menu', 'name', 'col_central', 'col_right', 'youtube', 'col_bottom_1', 'col_bottom_2', 'col_bottom_3', 'photo_alt', 'photo_description', 'meta_title', 'meta_description', 'meta_keywords', 'page__ptype')[0]
        except IndexError:
            raise Http404
        cols = ['col_bottom_1', 'col_bottom_2', 'col_bottom_3']  # some processing of the columns...
        page['bottom_cols'] = [page.pop(item) for item in cols if page[item]]

        page['youtube'] = self.get_youtube_embedded_url(page['youtube']) if page['youtube'] else ''

        return page

    def get_youtube_embedded_url(self, url):
        try:
            code = url.split('=')[-1]
            embedded_url = 'https://www.youtube.com/embed/' + code + '?feature=player_detailpage'
        except Exception:
            embedded_url = False
        return embedded_url
