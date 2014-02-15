import datetime
from django.test import TestCase
from django.test.client import Client
from apps.pages.models import Page, Page_translation


class ViewTestCase(TestCase):
    def setUp(self):
        some_page = Page.objects.create(id=1,
        slug='index',
        color='#FDA132',
        photo='images/photo.png',
        sortorder=1,
        status=1,
        ptype=1,
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
        updated_at=datetime.datetime.now(),
        created_at=datetime.datetime.now())
        
        self._client = Client()

    def test_view(self):

        response = self._client.get('/en/index.html')
        self.assertEqual(response.status_code, 200)
