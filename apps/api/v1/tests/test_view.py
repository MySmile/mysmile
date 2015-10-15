import datetime
from django.test import TestCase
from django.test.client import Client

from apps.pages.models import Page, Page_translation


class ApiTestCase(TestCase):
    def setUp(self):
        some_page = Page.objects.create(id=1,
                        slug='index',
                        color='#FDA132',
                        photo='images/photo.png',
                        sortorder=1,
                        status=Page.STATUS_PUBLISHED,
                        ptype=Page.PTYPE_API,
                        updated_at=datetime.datetime.now(),
                        created_at=datetime.datetime.now())
        
        Page_translation.objects.create(id=1,
                        page=some_page,
                        lang='en',
                        menu='Main',
                        col_central='lorem ipsum',
                        col_bottom_1='lorem ipsum',
                        col_bottom_2='lorem ipsum',
                        col_bottom_3='lorem ipsum',
                        meta_title='Welcome!',
                        meta_description='This is mane page!',
                        meta_keywords='Python3, Django',
                        photo_alt='',
                        photo_description='',
                        updated_at=datetime.datetime.now(),
                        created_at=datetime.datetime.now())
        self._client = Client()

    def test_content_short(self):
        response = self._client.get('/api/v1/content')
        self.assertEqual(response.status_code, 200)

    def test_content_slug(self):
        response = self._client.get('/api/v1/content?slug=index')
        self.assertEqual(response.status_code, 200)

    def test_content_slug_lang(self):
        response = self._client.get('/api/v1/content?slug=index&lang=en')
        self.assertEqual(response.status_code, 200)

    def test_language(self):
        response = self._client.get('/api/v1/language')
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self._client.get('/api/v1/contact')
        self.assertEqual(response.status_code, 200)
