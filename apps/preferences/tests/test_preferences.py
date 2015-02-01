import datetime
from django.test import TestCase
from django.test.client import Client

from apps.preferences.models import PreferencesManager


class PreferencesTestCase(TestCase):
    def setUp(self):
        self.preferences = PreferencesManager().get_all()

    def test_api_key_true(self):
        api_key = self.preferences.get('REST_API')
        self.assertEqual(api_key, 'True')
