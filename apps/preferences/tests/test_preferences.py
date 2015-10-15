from django.test import TestCase
from django.test.client import Client

from apps.preferences.models import PreferencesManager


class PreferencesTestCase(TestCase):
    fixtures = ['preferences.json']

    def setUp(self):
        pass

    def test_api_key_true(self):
        p = PreferencesManager().get_all()
        api_key = p.get('REST_API')
        self.assertEqual(api_key, 'True')

    def test_keys_true(self):
        p_keys = PreferencesManager().get_all().keys()

        self.assertTrue(len(p_keys) == 9)
        self.assertTrue('PHONE' in p_keys)
        self.assertTrue('EMAIL' in p_keys)
        self.assertTrue('SKYPE' in p_keys)
        self.assertTrue('GOOGLE_ANALITYCS_CODE' in p_keys)
        self.assertTrue('MAX_INNERLINK_HISTORY' in p_keys)
        self.assertTrue('REST_API' in p_keys)
        self.assertTrue('IMAGE_QUALITY' in p_keys)
        self.assertTrue('IMAGE_AUTOSCALE' in p_keys)
        self.assertTrue('THEME' in p_keys)

    def test_REST_API_switch(self):
        pass
