from django.http import HttpResponse

from mysmile.settings.main import LANGUAGES
from apps.pages.models import Page_translation


def createNode(url, modified):
    return '<url><loc>' + url + '</loc><changefreq>weekly</changefreq>\
<lastmod>' + modified + '</lastmod></url>'

def SitemapXML(request):
    xml = '<?xml version = "1.0" encoding = "UTF-8"?>\
    <urlset xmlns = "http://www.sitemaps.org/schemas/sitemap/0.9">'
    langs_and_slugs = Page_translation.objects.filter(page__status=1, page__ptype__in = [0,1]).values('lang', 'page__slug', 'updated_at').order_by('lang')
    for item in langs_and_slugs:
        url = 'http://' + request.META['HTTP_HOST'] + '/' + item['lang'] + '/' + item['page__slug'] + '.html'
        modified = item['updated_at'].strftime('%Y-%m-%d')
        xml += createNode(url, modified)
    xml += '</urlset>'
    return HttpResponse(xml, mimetype="text/xml")
