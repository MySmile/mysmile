from django.db import models, IntegrityError
from django.http import Http404
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from mysmile.settings.main import LANGUAGES 
from apps.pages.models import Page, Page_translation
from apps.settings.managers import SettingsManager


class PagesManager(models.Manager):

    def get_content(self, request, lang=None, slug=None):
        c = {'lang': lang, 'slug': slug}

        try:
            c = self.get_page(lang, slug)
            c['main_menu'] = self.get_main_menu(lang)
            sm = SettingsManager()
            c['inav'] = self.get_additional_dynamic_menu(request, c['main_menu'], slug, int(sm.get('MAX_INNERLINK_HISTORY').get('MAX_INNERLINK_HISTORY')))

            c.update(sm.get_contact())
            c.update(sm.get('GOOGLE_ANALITYCS_CODE'))

        except IndexError:
            raise Http404
        except IntegrityError: # database error
            pass


        c['languages'] = LANGUAGES if len(LANGUAGES) > 1 else ''

        return c

    def get_main_menu(self, lang):
            menues = Page_translation.objects.filter(lang=lang, page__status=Page.STATUS_PUBLISHED, page__ptype__in=[Page.PTYPE_MENU,Page.PTYPE_MENU_API]).values('page__slug', 'menu').order_by('page__sortorder')
            return menues


    def get_additional_dynamic_menu(self, request, menu, slug, max_innerlink_history):
        inner_nav = request.session.get('inner_nav', [])
        if Page.objects.filter(slug=slug, ptype=Page.PTYPE_INNER):
            #~ max_innerlink_history = 10 
            # FIXME! #int(APP_SETTINGS['MAX_INNERLINK_HISTORY'])
            temp = [slug, menu]
            if not temp in inner_nav:  # work with sessions
                inner_nav.append([slug, menu])
                request.session['inner_nav'] = inner_nav  # save data to the session
                while len(inner_nav) > max_innerlink_history:
                    inner_nav.pop(0)
        return inner_nav

    #~ def get_contact(self, request, menu, slug):
        #~ contact = make_template_fragment_key('block_contact')
        #~ if not cache.get(key):
            #~ app_settings = Settings.objects.filter(key__in = ['PHONE', 'EMAIL', 'SKYPE', 'GOOGLE_ANALITYCS_CODE']).values('key','value')
            #~ print('app_settings = ', app_settings)
            #~ for item in app_settings:
                #~ c.update({item['key']:item['value']})
        #~ return inner_nav

    def get_page(self, lang, slug):

        #~ page_id = Page.objects.filter(slug=slug, status=Page.STATUS_PUBLISHED).values('id')
        page = Page_translation.objects.filter(lang=lang, page__ptype__in = [Page.PTYPE_INNER,Page.PTYPE_MENU,Page.PTYPE_MENU_API], page__status=Page.STATUS_PUBLISHED, page__slug=slug).values('page__color', 'page__photo', 'menu', 'name', 'col_central', 'col_right', 'youtube', 'col_bottom_1', 'col_bottom_2', 'col_bottom_3', 'photo_alt', 'photo_description', 'meta_title', 'meta_description', 'meta_keywords')[0]

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
