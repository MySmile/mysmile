from django.db import models
from mysmile.user_settings import user_settings


class Page(models.Model):
    slug = models.SlugField(unique=True,
                            help_text='This is unique. Valid characters \
                                       of the alphabet in upper lower case, \
                                       and the hyphen (not underscore!)')
    color = models.CharField(max_length=7, default='#FDA132',
                             help_text='Click once with the mouse to select \
                                        a color, and then twice to save')
    # blank=True add "clear image" checkbox into admin page
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    sortorder = models.IntegerField(unique=True)
    status = models.IntegerField(unique=False, choices=((0, 'draft'),
                                 (1, 'published'),), default=0)
    ptype = models.IntegerField(unique=False, choices=((0, 'inner page'),
                                (1, 'menu page'),), default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.slug

    class Meta:
        db_table = 'Page'
        ordering = ['-ptype', 'sortorder', 'status']


class Page_translation(models.Model):
    ALL_LANGS_DESC = []
    for i in user_settings['ALL_LANGS']:
        ALL_LANGS_DESC.append((i, i))
    ALL_LANGS_DESC = tuple(ALL_LANGS_DESC)

    page = models.ForeignKey(Page)
    lang = models.CharField(max_length=2, choices=ALL_LANGS_DESC,
                            default=user_settings['ALL_LANGS'][0])
    menu = models.CharField(max_length=200)
    name = models.CharField(max_length=200, blank=True, null=True)
    central_col = models.TextField(blank=False, null=False)
    youtube = models.CharField(max_length=2048, blank=True, null=True,
                               help_text='Link to youtube video. \
                               Max length url =  2048 characters')
    right_col = models.TextField(blank=True, null=True)
    bottom_col1 = models.TextField(blank=True, null=True)
    bottom_col2 = models.TextField(blank=True, null=True)
    bottom_col3 = models.TextField(blank=True, null=True)

    meta_title = models.CharField(max_length=500)
    meta_description = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=500)
    photo_alt = models.CharField(max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.lang

    class Meta:
        db_table = 'Page_translation'
        ordering = ['lang']
        verbose_name = 'Translation'
        verbose_name_plural = 'Translations'
