from django.db import models

from mysmile.settings.base import LANGUAGES


class Page(models.Model):
    PTYPE_INNER = 0
    PTYPE_MENU = 1
    PTYPE_API = 2
    PTYPE_MENU_API = 3
    PTYPE = ((PTYPE_INNER, 'inner page'), # website only
             (PTYPE_MENU, 'menu page'), # website only
             (PTYPE_API, 'api page'),  # api only
             (PTYPE_MENU_API, 'api & menu page'))  # api & website

    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1
    STATUS = ((STATUS_DRAFT, 'draft'),
              (STATUS_PUBLISHED, 'published'))
    SORTORDER_STEP = 10

    slug = models.SlugField(unique=True,)
    color = models.CharField(max_length=500, default='#FDA132',
                             help_text='Click once with the mouse to select \
                                        a color, and then twice to save')
    # blank=True add "clear image" checkbox into admin page
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    sortorder = models.IntegerField(unique=True, default=lambda: Page.objects.all().aggregate(models.Max('sortorder'))['sortorder__max']+Page.SORTORDER_STEP, verbose_name='Sort order')
    status = models.IntegerField(unique=False, choices=STATUS, default=STATUS_DRAFT)
    ptype = models.IntegerField(unique=False, choices=PTYPE, default=PTYPE_MENU, verbose_name='Page type')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def photo_thumb(self):
        if self.photo:
            return '<img src="' + self.photo.url + '" height="48"/>'
        else:
            return ''
    photo_thumb.allow_tags = True

    def __setattr__(self, name, value):
        if name.isupper():
            raise AttributeError(name + " is an immutable attribute.")
        else:
            self.__dict__[name] = value
            
    def __unicode__(self):
        return self.slug

    class Meta:
        db_table = 'Page'
        ordering = ['-ptype', 'sortorder', 'status']


class Page_translation(models.Model):
    page = models.ForeignKey(Page)
    lang = models.CharField(max_length=500, choices=LANGUAGES,
                            default=LANGUAGES[0][0])
    menu = models.CharField(max_length=500)
    name = models.CharField(max_length=500, blank=True, null=True)
    col_central = models.TextField(blank=False, null=False)
    youtube = models.CharField(max_length=500, blank=True, null=True,
                               help_text='Link to youtube video. \
                               Max length url =  2048 characters')
    col_right = models.TextField(blank=True, null=True)
    col_bottom_1 = models.TextField(blank=True, null=True)
    col_bottom_2 = models.TextField(blank=True, null=True)
    col_bottom_3 = models.TextField(blank=True, null=True)

    meta_title = models.CharField(max_length=500)
    meta_description = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=500)
    photo_alt = models.CharField(max_length=500, blank=True, null=True)
    photo_description = models.CharField(max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.lang

    class Meta:
        db_table = 'Page_translation'
        ordering = ['lang']
        verbose_name = 'Translation'
        verbose_name_plural = 'Translations'
        unique_together = ('page', 'lang')


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
