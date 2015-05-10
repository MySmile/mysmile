import datetime
from django.test import TestCase
from apps.pages.models import Page, Page_translation


class Page_translationTestCase(TestCase):
    def setUp(self):
        some_page = Page.objects.create(id=1,
        slug='index',
        color='#FDA132',
        photo='images/photo.png',
        sortorder=10,
        status=Page.STATUS_PUBLISHED,
        ptype=Page.PTYPE_MENU,
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

    def test_page_translation_create(self):
        first_page_translation = Page_translation.objects.get(id=1)
        self.assertEqual(first_page_translation.page_id, 1)

