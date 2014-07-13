from django.db import models

from mysmile.settings.base import LANGUAGES


class Page(models.Model):
    PTYPE_INNER = 0
    PTYPE_MENU = 1
    PTYPE_API = 2
    PTYPE_MENU_API = 3
    PTYPE = ((PTYPE_INNER, 'inner page'),
             (PTYPE_MENU, 'menu page'),
             (PTYPE_API, 'api page'),
             (PTYPE_MENU_API, 'api & menu page'))

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
    sortorder = models.IntegerField(unique=True, default=lambda: Page.objects.all().aggregate(models.Max('sortorder'))['sortorder__max']+SORTORDER_STEP)
    status = models.IntegerField(unique=False, choices=STATUS, default=STATUS_DRAFT)
    ptype = models.IntegerField(unique=False, choices=PTYPE, default=PTYPE_MENU)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def photo_thumb(self):
        if self.photo:
            return '<img src="' + self.photo.url + '" height="48"/>'
        else:
            return ''
    photo_thumb.allow_tags = True
    
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
    phone = models.CharField(blank=True, null=True, max_length=500)
    email = models.CharField(blank=True, null=True, max_length=500)
    skype = models.CharField(blank=True, null=True, max_length=500)
    google_code = models.CharField(blank=True, null=True, max_length=500)
    max_inner_link = models.IntegerField(blank=True, null=True)
    rest_api = models.IntegerField(choices=((1, 'True'), (0, 'False')), default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Settings'
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'
#~ 
#~ class Settings(models.Model):
    #~ key = models.CharField(unique=True, max_length=500)
    #~ value = models.CharField(blank=True, null=True, max_length=500)
    #~ name = models.CharField(max_length=500)
    #~ description = models.CharField(max_length=500)
    #~ created_at = models.DateTimeField(auto_now_add=True)
    #~ updated_at = models.DateTimeField(auto_now=True)
    #~ 
    #~ class Meta:
        #~ db_table = 'Settings'
        #~ verbose_name = 'Setting'
        #~ verbose_name_plural = 'Settings'
#~ 
