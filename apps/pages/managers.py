from datetime import datetime

from django.db import models
from django.http import Http404

from mysmile.settings import LANGUAGES
from mysmile.user_settings import user_settings
from apps.pages.models import Page, Page_translation


class PagesManager(models.Manager):

    def get_content(self, request, lang=None, slug=None):
        page_id = Page.objects.filter(slug=slug, status=1).values('id')
        content = Page_translation.objects.filter(lang=lang, page__status=1, page_id=page_id).values('page__color', 'page__photo', 'menu', 'name', 'central_col', 'right_col', 'youtube', 'bottom_col1', 'bottom_col2', 'bottom_col3', 'photo_alt', 'meta_title', 'meta_description', 'meta_keywords')
        c = {}
        cols = ['bottom_col1', 'bottom_col2', 'bottom_col3']  # some processing of the columns...
        try:
            c['bottom_cols'] = [content[0].pop(item) for item in cols if content[0][item]]
            c['inav'] = self.get_inner_nav(request, content[0]['menu'], slug)
        except IndexError:
            raise Http404

        slugs = Page.objects.filter(status=1, ptype=1).values_list('slug', flat=True).order_by('sortorder')
        menues = Page_translation.objects.filter(lang=lang, page__status=1, page__ptype=1).values_list( 'menu', flat=True).order_by('page__sortorder')
        c['nav'] = list(map(lambda x, y: (x, y), slugs, menues))

        c['languages'] = LANGUAGES
        c['logo_link'] = '/' + lang + '/' + self.get_first_slug() + '.html'
        c['lang'] = lang
        c['slug'] = slug
        c['current_year'] = datetime.now().strftime('%Y')

        c.update(user_settings)
        c.update(content[0])

        if c['youtube']:
            c['youtube'] = self.get_youtube_embedded_url(c['youtube'])
        return c

    def get_inner_nav(self, request, menu, slug):
        inner_nav = request.session.get('inner_nav', [])
        if Page.objects.filter(slug=slug, ptype=0):  # ptype=0 --- value for inner_page
            while len(inner_nav) > user_settings['MAX_INNERLINK_HISTORY']:
                inner_nav.pop(0)
            temp = [slug, menu]
            if not temp in inner_nav:  # work with sessions
                inner_nav.append([slug, menu])
                request.session['inner_nav'] = inner_nav  # save data to the session
        return inner_nav

    def get_first_slug(self):
        return Page.objects.filter(status=1, ptype=1).values_list('slug', flat=True).order_by('sortorder').first()

    def get_youtube_embedded_url(self, url):
        try:
            code = url.split('=')[-1]
            embedded_url = 'https://www.youtube.com/embed/' + code + '?feature=player_detailpage'
        except Exception:
            embedded_url = False
        return embedded_url
