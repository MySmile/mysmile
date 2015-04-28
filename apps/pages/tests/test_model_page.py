import datetime
from django.test import TestCase
from apps.pages.models import Page


class PageTestCase(TestCase):
    def setUp(self):
        Page.objects.create(id=1,
        slug='index',
        color='#FDA132',
        photo='images/photo.png',
        sortorder=10,
        status=Page.STATUS_PUBLISHED,
        ptype=Page.PTYPE_MENU,
        updated_at=datetime.datetime.now(),
        created_at=datetime.datetime.now())
        
        Page.objects.create(id=2,
        slug='contacts',
        color='#DDD',
        photo='',
        sortorder=2,
        status=0,
        ptype=0,
        updated_at=datetime.datetime.now(),
        created_at=datetime.datetime.now())

    def test_page_create(self):
        first_page = Page.objects.get(id=1)
        second_page = Page.objects.get(id=2)
        self.assertEqual(first_page.slug, 'index')
        self.assertEqual(second_page.slug, 'contacts')
    
    def test_page_status(self):
        first_page = Page.objects.get(id=1)
        self.assertEqual(first_page.status, 1)
        first_page.status = 0
        self.assertEqual(first_page.status, 0)

