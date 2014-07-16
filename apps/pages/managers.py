from django.db import models, IntegrityError
from django.http import Http404
from django.core.cache import cache
from django.core.cache import get_cache
from django.core.cache.utils import make_template_fragment_key

from mysmile.settings.main import LANGUAGES
from apps.pages.models import Page, Page_translation, Settings


class PagesManager(models.Manager):

    def get_content(self, request, lang=None, slug=None):
        try:
            page_id = Page.objects.filter(slug=slug, status=Page.STATUS_PUBLISHED).values('id')
            content = Page_translation.objects.filter(lang=lang, page__ptype__in = [Page.PTYPE_INNER,Page.PTYPE_MENU], page__status=Page.STATUS_PUBLISHED, page_id=page_id).values('page__color', 'page__photo', 'menu', 'name', 'col_central', 'col_right', 'youtube', 'col_bottom_1', 'col_bottom_2', 'col_bottom_3', 'photo_alt', 'photo_description', 'meta_title', 'meta_description', 'meta_keywords')

            slugs = Page.objects.filter(status=Page.STATUS_PUBLISHED, ptype=Page.PTYPE_MENU).values_list('slug', flat=True).order_by('sortorder')
            menues = Page_translation.objects.filter(lang=lang, page__status=Page.STATUS_PUBLISHED, page__ptype=Page.PTYPE_MENU).values_list('menu', flat=True).order_by('page__sortorder')

            c = content[0] if content else {}
            key = make_template_fragment_key('block_contact')
            if not cache.get(key):
                print('CREATE NEW CAHE!')
                contact = Settings.objects.filter(key__in = ['KEY_PHONE', 'KEY_EMAIL', 'KEY_SKYPE', 'KEY_GOOGLE_ANALITYCS_CODE']).values('key','value')
                for item in contact:
                    c.update({item['key']:item['value']})

            cols = ['col_bottom_1', 'col_bottom_2', 'col_bottom_3']  # some processing of the columns...
            c['bottom_cols'] = [content[0].pop(item) for item in cols if content[0][item]]
            c['inav'] = self.get_inner_nav(request, c['menu'], slug)
        except IndexError:
            raise Http404
        except IntegrityError: # database error
            pass

        c['nav'] = list(map(lambda x, y: (x, y), slugs, menues))

        c['languages'] = LANGUAGES if len(LANGUAGES) > 1 else ''
        c['lang'], c['slug'] = lang, slug
        c['youtube'] = self.get_youtube_embedded_url(c['youtube']) if c['youtube'] else ''

        return c

    def get_inner_nav(self, request, menu, slug):
        inner_nav = request.session.get('inner_nav', [])
        if Page.objects.filter(slug=slug, ptype=Page.PTYPE_INNER):
            max_innerlink_history = int(Settings.objects.filter(key = 'KEY_MAX_INNERLINK_HISTORY').values_list('value', flat=True)[0])
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
