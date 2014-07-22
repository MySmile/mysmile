from django.db import models, IntegrityError
from django.http import Http404
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from mysmile.settings.main import LANGUAGES, APP_SETTINGS
from apps.pages.models import Page, Page_translation, Settings


class PagesManager(models.Manager):

    def get_content(self, request, lang=None, slug=None):
        try:
            page_id = Page.objects.filter(slug=slug, status=Page.STATUS_PUBLISHED).values('id')
            content = Page_translation.objects.filter(lang=lang, page__ptype__in = [Page.PTYPE_INNER,Page.PTYPE_MENU,Page.PTYPE_MENU_API], page__status=Page.STATUS_PUBLISHED, page_id=page_id).values('page__color', 'page__photo', 'menu', 'name', 'col_central', 'col_right', 'youtube', 'col_bottom_1', 'col_bottom_2', 'col_bottom_3', 'photo_alt', 'photo_description', 'meta_title', 'meta_description', 'meta_keywords')

            c = content[0] if content else {}
            
            slugs = Page.objects.filter(status=Page.STATUS_PUBLISHED, ptype__in=[Page.PTYPE_MENU,Page.PTYPE_MENU_API]).values_list('slug', flat=True).order_by('sortorder')
            menues = Page_translation.objects.filter(lang=lang, page__status=Page.STATUS_PUBLISHED, page__ptype__in=[Page.PTYPE_MENU,Page.PTYPE_MENU_API]).values_list('menu', flat=True).order_by('page__sortorder')
            c['nav'] = list(map(lambda x, y: (x, y), slugs, menues))

            key = make_template_fragment_key('block_contact')
            if not cache.get(key):
                c.update(APP_SETTINGS)
                
            cols = ['col_bottom_1', 'col_bottom_2', 'col_bottom_3']  # some processing of the columns...
            c['bottom_cols'] = [content[0].pop(item) for item in cols if content[0][item]]
            c['inav'] = self.get_inner_nav(request, c['menu'], slug)
        except IndexError:
            raise Http404
        except IntegrityError: # database error
            pass

        #~ print('aaps/pages/managers.py: APP_SETTINGS = ', APP_SETTINGS)

        c['languages'] = LANGUAGES if len(LANGUAGES) > 1 else ''
        c['lang'], c['slug'] = lang, slug
        c['youtube'] = self.get_youtube_embedded_url(c['youtube']) if c['youtube'] else ''

        return c

    def get_inner_nav(self, request, menu, slug):
        inner_nav = request.session.get('inner_nav', [])
        if Page.objects.filter(slug=slug, ptype=Page.PTYPE_INNER):
            max_innerlink_history = int(APP_SETTINGS['MAX_INNERLINK_HISTORY'])
            temp = [slug, menu]
            if not temp in inner_nav:  # work with sessions
                inner_nav.append([slug, menu])
                request.session['inner_nav'] = inner_nav  # save data to the session
                while len(inner_nav) > max_innerlink_history:
                    inner_nav.pop(0)
        return inner_nav

    def get_youtube_embedded_url(self, url):
        try:
            code = url.split('=')[-1]
            embedded_url = 'https://www.youtube.com/embed/' + code + '?feature=player_detailpage'
        except Exception:
            embedded_url = False
        return embedded_url
