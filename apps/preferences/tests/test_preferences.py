import datetime
from django.test import TestCase
from django.test.client import Client

from apps.preferences.models import Preferences, PreferencesManager


class PreferencesTestCase(TestCase):
    def setUp(self):

        Preferences.objects.create(id=1,
        key='REST_API',
        value='True',
        name='Turn on/off REST Api',
        description='Turn on/off alternative way of getting pages using REST api. Only a special marked pages can be available for api. For more information please look into page statuses list.',
        updated_at=datetime.datetime.now(),
        created_at=datetime.datetime.now())
        self.preferences = PreferencesManager().get_all()

    def test_api_key_true(self):
        api_key = self.preferences.get('REST_API')
        self.assertEqual(api_key, 'True')
