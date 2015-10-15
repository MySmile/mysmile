import datetime
from django.test import TestCase
from django.test.client import Client


class SitemapTestView(TestCase):
    fixtures = ['apps/pages/fixtures/pages.json']

    def setUp(self):
        self._client = Client()
        self.response = self._client.get('/Sitemap.xml', HTTP_HOST="testdomain.com")

    def test_sitemap(self):
        self.assertEqual(self.response.status_code, 200)

    def test_item_index(self):
        self.assertIn(b'index.html', self.response.content)
