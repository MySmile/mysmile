from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import datetime
import logging

# import user settings PHONE, EMAIL, etc.
from mysmile.user_settings import user_settings
# manager all connection to db
from pages.managers import PagesManager
from pages.decorators import ls_check

logger = logging.getLogger(__name__)  # Get an instance of a logger


@ls_check
def page(request, lang='', slug=''):  # c={}):
    w = PagesManager()
    c = w.get_content(lang, slug)
    c['nav'] = w.get_nav(lang)
    c['menu_flag'] = w.get_menu_flags(slug)
    c['inav'] = w.get_inner_nav(request, c['menu'], slug)
    c['logo_link'] = '/' + lang + '/' + w.get_first_slug() + '.html'
    c['lang'] = lang
    c['slug'] = slug

    c.update(user_settings)
    c['current_year'] = datetime.datetime.now().strftime('%Y')

    t = get_template('pages/page.html')
    html = t.render(Context(c))
    return HttpResponse(html)
