from django.test import TestCase

from django.utils import timezone

from apps.pages.models import Page


class PageTestCase(TestCase):
    fixtures = ['pages.json']

    def setUp(self):
        pass

    def test_page_field_created_at(self):
        pass
        # p = Page.objects.create(
        # slug='slug',
        # color='#FDA132',
        # photo='images/photo.png',
        # status=Page.STATUS_PUBLISHED,
        # ptype=Page.PTYPE_MENU)
        # p.save()
        # # local = timezone.localtime(timezone.now())
        # local = timezone.now()
        # created_at = p.created_at
        # delta = (local-created_at).total_seconds() # in seconds
        # self.assertTrue(delta<5)



