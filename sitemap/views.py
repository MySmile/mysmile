from pages.models import Page, Page_translation
from django.http import HttpResponse
from mysmile import user_settings

from pages.managers import PagesManager

def createNode(url, modified):
    return '<url><loc>' + url + '</loc><changefreq>weekly</changefreq>\
<lastmod>' + modified + '</lastmod></url>'

def SitemapXML(request):
    xml='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    w = PagesManager()
    slug_pages = w.get_slug_published()#Page.objects.raw('SELECT id, slug FROM page WHERE status=1')
    for i in slug_pages:
        p_trans = w.get_data_for_node(i.id)
        for j in p_trans:
            url = user_settings.DOMAIN_NAME + j.lang + '/' + i.slug + '.html'
            modified = j.updated_at.strftime('%Y-%m-%d')
            xml += createNode(url, modified)
    xml += '</urlset>'
    return HttpResponse(xml, mimetype="text/xml")
