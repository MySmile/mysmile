from pages.models import Page, Page_translation
from django.http import HttpResponse
from mysmile import user_settings


def createNode(url, modified):
	return '<url><loc>' + url + '</loc><changefreq>weekly</changefreq>\
<lastmod>' + modified + '</lastmod></url>'


def SitemapXML(request):
	xml='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
	
	slug_pages = Page.objects.raw('SELECT id, slug FROM page WHERE status=1')
	for i in slug_pages:
		query = 'SELECT id,lang,updated_at FROM page_translation WHERE page_id=%s' % i.id
		p_trans = Page_translation.objects.raw(query)

		for j in p_trans:
			url = user_settings.DOMAIN_NAME + j.lang + '/' + i.slug + '.html'
			modified = j.updated_at.strftime('%Y-%m-%d')
			xml += createNode(url, modified)
	xml += '</urlset>'
	return HttpResponse(xml, mimetype="text/xml")
