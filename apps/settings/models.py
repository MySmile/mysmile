from django.db import models


class Settings(models.Model):
    KEY_PHONE = 'PHONE'
    KEY_EMAIL = 'EMAIL'
    KEY_SKYPE = 'SKYPE'
    KEY_GOOGLE_ANALITYCS_CODE = 'GOOGLE_ANALITYCS_CODE'
    KEY_MAX_INNERLINK_HISTORY = 'MAX_INNERLINK_HISTORY'
    KEY_REST_API = 'REST_API'

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
                'name': 'Turn on/off REST Api', 'description': 'Turn on/off alternative way of getting pages using REST api. Only a special marked pages can be available for api. For more information please look into page statuses list.'})

    key = models.CharField(unique=True, max_length=500)
    value = models.CharField(blank=True, null=True, max_length=500)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __setattr__(self, name, value):
        if name.isupper():
            raise AttributeError(name + " is an immutable attribute.")
        else:
            self.__dict__[name] = value

    class Meta:
        db_table = 'Settings'
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

