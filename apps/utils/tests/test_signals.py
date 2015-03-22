import datetime
from django.test import TestCase
from django.test.client import Client

from apps.pages.models import Page, Page_translation
from django.conf import settings

class SignalsTestCase(TestCase):
    def setUp(self):
        # @TODO create testphoto.png with pillow
        pass
    def test_clear_photo_file(self):
        pass