from django.db import models
from django.db import connection
#from django.http import HttpRequest
#from django.contrib.sessions.backends.db import SessionStore
from django.http import Http404

from mysmile.user_settings import user_settings
from pages.models import Page, Page_translation


class PagesManager(models.Manager):

    def get_first_slug(self):
        #refactoring below
        return Page.objects.raw('SELECT id,slug FROM Page \
                                ORDER BY sortorder ASC')[0].slug

    def get_nav(self, lang):
        cursor = connection.cursor()
        cursor.execute('SELECT P.slug, PT.menu \
                       FROM Page P, Page_translation PT WHERE \
            P.id = PT.page_id and P.status = 1 and P.ptype = 1 \
                   and PT.lang = %s ORDER BY P.sortorder', [lang])
        return cursor.fetchall()

    def get_inner_nav(self, request, menu, slug0):
        inner_nav = request.session.get('inner_nav', [])
        if Page.objects.filter(slug=slug0, ptype=0):  # ptype=0 --- inner_page
            while len(inner_nav) > user_settings['MAX_INNERLINK_HISTORY']:
                inner_nav.pop(0)
            temp = [slug0, menu]
            # work with sessions
            if not temp in inner_nav:
                inner_nav.append([slug0, menu])
                # save data to the session
                request.session['inner_nav'] = inner_nav
        return inner_nav

    def get_menu_flags(self, slug):
        cursor = connection.cursor()
        cursor.execute('SELECT PT.lang FROM Page P, Page_translation PT WHERE \
            P.id = PT.page_id and P.status = 1 and P.slug = %s', [slug])
        return list(list(i)[0] for i in cursor.fetchall())

    def get_content(self, lang0, slug0):
        try:
            c = Page.objects.filter(slug=slug0).values('id', 'color',
                                                       'photo')[0]
            cc = Page_translation.objects.filter(page_id=c['id'], lang=lang0)
            cc = cc.values('meta_title', 'meta_description', 'meta_keywords',
                           'photo_alt', 'menu', 'name', 'central_col',
                           'right_col', 'youtube', 'bottom_col1',
                           'bottom_col2', 'bottom_col3')[0]
        except:
            raise Http404
        cc['bottom_cols'] = []  # some processing of the columns...
        if cc['bottom_col1']:
            cc['bottom_cols'].append(cc['bottom_col1'])
        if cc['bottom_col2']:
            cc['bottom_cols'].append(cc['bottom_col2'])
        if cc['bottom_col3']:
            cc['bottom_cols'].append(cc['bottom_col3'])
        if cc['youtube']:
            cc['youtube'] = 'https://www.youtube.com/embed/' + \
                            cc['youtube'].split('=')[-1] + \
                            '?feature = player_detailpage'
        cc.update(c)
        return cc

    def get_slug_published(self):
        return Page.objects.raw('SELECT id, slug FROM page WHERE status=1')

    def get_data_for_node(self, id):
        return  Page_translation.objects.raw('SELECT id, lang, updated_at \
                                             FROM page_translation \
                                             WHERE page_id = %s', [id])
