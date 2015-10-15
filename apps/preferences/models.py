from django.db import models
from django.utils.translation import ugettext_lazy as _


class PreferencesManager(models.Manager):
    def get_all(self):
        p = Preferences.objects.all().values('key', 'value')
        c = {}
        for item in p:
            c[item['key']] = item['value']
        return c

    def get_contact(self):
        p = Preferences.objects.filter(key__in=['PHONE', 'EMAIL', 'SKYPE']).values('key', 'value')
        c = {}
        for item in p:
            c[item['key'].lower()] = item['value']
        return c


class Preferences(models.Model):
    KEY_PHONE = 'PHONE'
    KEY_EMAIL = 'EMAIL'
    KEY_SKYPE = 'SKYPE'
    KEY_GOOGLE_ANALITYCS_CODE = 'GOOGLE_ANALITYCS_CODE'
    KEY_MAX_INNERLINK_HISTORY = 'MAX_INNERLINK_HISTORY'
    KEY_REST_API = 'REST_API'
    KEY_IMAGE_QUALITY = 'IMAGE_QUALITY'
    KEY_THEME = 'THEME'
    KEY_IMAGE_AUTOSCALE = 'IMAGE_AUTOSCALE'

    CONTACT = {KEY_PHONE: 'phone', KEY_EMAIL: 'email', KEY_SKYPE: 'skype'}

    DEFAULT = ({'key': KEY_PHONE, 'value': '000 000 000 00 00',
                'name': 'Phone number', 'description': 'Contact phone number. It is visible on the top of site page.'},
               {'key': KEY_EMAIL, 'value': 'myemail@email.com',
                'name': 'Email', 'description': 'Contact Email. It is visible on the top of site page as an image to protect from spam bot.'},
               {'key': KEY_SKYPE, 'value': 'myskype',
                'name': 'Skype', 'description': 'Contact skype. It is visible on the top of site page.'},
               {'key': KEY_GOOGLE_ANALITYCS_CODE, 'value': '',
                'name': 'Google Analytic code', 'description': 'Code uses to connect to Google Analytic service.'},
               {'key': KEY_MAX_INNERLINK_HISTORY, 'value': 4,
                'name': 'Max number of inner pages', 'description': 'Number of pages that can be shown under main menu when user follow links inside page. Generally inner pages used only as a link inside content.'},
               {'key': KEY_REST_API, 'value': True,
                'name': 'Turn on/off REST Api', 'description': 'Turn on/off alternative way of getting pages using REST api. Only a special marked pages can be available for api. For more information please look into page statuses list.'},
               {'key': KEY_IMAGE_QUALITY, 'value': 100,
                'name': 'Image quality', 'description': 'Global setting quality uploaded pictures. The picture quality is directly proportional to the size of the file. A value of 100 corresponds to the maximum quality.'},
               {'key': KEY_THEME, 'value': 'modern',
                'name': 'Theme switcher', 'description': 'Choose a theme for switch'},
               {'key': KEY_IMAGE_AUTOSCALE, 'value': True,
                'name': 'Image autoscale', 'description': 'Global setting for autoscale uploaded pictures if its width>333px. Pictures will be scaled to width=333px.'},)

    key = models.CharField(unique=True, max_length=255, verbose_name=_('key'))
    value = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('value'))
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.CharField(max_length=255, verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PreferencesManager()

    def __setattr__(self, name, value):
        if name.isupper():
            raise AttributeError(name + " is an immutable attribute.")
        else:
            self.__dict__[name] = value

    class Meta:
        db_table = 'Preferences'
        ordering = ['name']
        verbose_name = _('Preference')
        verbose_name_plural = _('Preferences')

