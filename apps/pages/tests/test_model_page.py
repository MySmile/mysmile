import datetime
from django.test import TestCase
from apps.pages.models import Page


class PageTestCase(TestCase):
    fixtures = ['pages.json']

    def setUp(self):
        pass

    def test_photo_thumb(self):
        pass



