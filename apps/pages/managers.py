from django.db import models
from django.http import Http404

from apps.pages.models import Page, Page_translation


class PagesManager(models.Manager):
    
    # def __init__(self):
        # SettingsManager.__init__(self)

    def get_content(self, lang=None, slug=None):
        c = self.get_page(lang, slug)
        # c.update({'lang': lang, 'slug': slug})
        # c.update(signing.loads(cache.get('app_settings')))

        c['main_menu'] = self.get_main_menu(lang)
        return c

    def get_main_menu(self, lang):
        main_menu = Page_translation.objects.filter(lang=lang, page__status=Page.STATUS_PUBLISHED, page__ptype__in=[Page.PTYPE_MENU,Page.PTYPE_MENU_API]).values('page__slug', 'menu').order_by('page__sortorder')
        return main_menu

    def get_page(self, lang, slug):
        try:
            page = Page_translation.objects.filter(lang=lang, page__ptype__in = [Page.PTYPE_INNER,Page.PTYPE_MENU,Page.PTYPE_MENU_API], page__status=Page.STATUS_PUBLISHED, page__slug=slug).values('page__color', 'page__photo', 'menu', 'name', 'col_central', 'col_right', 'youtube', 'col_bottom_1', 'col_bottom_2', 'col_bottom_3', 'photo_alt', 'photo_description', 'meta_title', 'meta_description', 'meta_keywords', 'page__ptype')[0]
        except IndexError:
            raise Http404

        page['bottom_cols'] = list(filter(None, [page['col_bottom_1'], page['col_bottom_2'], page['col_bottom_3']]))
        return page
