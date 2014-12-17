import datetime
from django.test import TestCase
from django.test.client import Client
#~ from apps.settings.models import Settings
from apps.settings.managers import SettingsManager


class SettingsTestCase(TestCase):
    def setUp(self):
        self.settings = SettingsManager()
        
    def test_api_key_true(self):
        api_key = self.settings.get('REST_API')
        self.assertEqual(api_key, 'True')
