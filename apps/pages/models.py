from django.db import models
from django.http import Http404
# from django.db import connections, transaction
# from django.db.models.signals import post_save
# from django.conf import settings

from mysmile.settings.base import LANGUAGES


class ImageField(models.ImageField):

    def save_form_data(self, instance, data):
        if data is not None:
            file = getattr(instance, self.attname)
            if file != data:
                file.delete(save=False)
        super(ImageField, self).save_form_data(instance, data)


class PagesManager(models.Manager):
    def get_content(self, lang=None, slug=None):
        c = self.get_page(lang, slug)
        c['main_menu'] = self.get_main_menu(lang)
        return c

    def get_main_menu(self, lang):
        main_menu = Page_translation.objects.filter(lang=lang, page__status=Page.STATUS_PUBLISHED, page__ptype__in=[Page.PTYPE_MENU,Page.PTYPE_MENU_API]).values('page__slug', 'menu').order_by('page__sortorder')
        return main_menu

    def get_page(self, lang, slug):
        try:
            page = Page_translation.objects.filter(lang=lang, page__ptype__in = [Page.PTYPE_INNER,Page.PTYPE_MENU,Page.PTYPE_MENU_API], page__status=Page.STATUS_PUBLISHED, page__slug=slug).values('page__color', 'page__photo', 'menu', 'name', 'col_central', 'col_right', 'youtube', 'col_bottom_1', 'col_bottom_2', 'col_bottom_3', 'photo_alt', 'photo_description', 'meta_title', 'meta_description', 'meta_keywords', 'page__ptype')[0]
        except IndexError:
            raise Http404

        page['bottom_cols'] = list(filter(None, [page['col_bottom_1'], page['col_bottom_2'], page['col_bottom_3']]))
        return page


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
    photo = ImageField(upload_to='images/', null=True, blank=True)
    sortorder = models.IntegerField(unique=True, default=lambda: Page.objects.all().aggregate(models.Max('sortorder'))['sortorder__max']+Page.SORTORDER_STEP, verbose_name='Sort order')
    status = models.IntegerField(unique=False, choices=STATUS, default=STATUS_DRAFT)
    ptype = models.IntegerField(unique=False, choices=PTYPE, default=PTYPE_MENU, verbose_name='Page type')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PagesManager()

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

#
# # post_save signals for clear cache
# def clear_cache(sender, instance, **kwargs):
#     print('Cache before clearing')
#     cursor = connections['default'].cursor()
#     cache_table = settings.CACHES['default']['LOCATION']
#     cursor.execute(' '.join(['DELETE FROM ', cache_table]))
#     transaction.commit_unless_managed(using='default')
#     print('AFTER before clearing.......')
#
# # register the signal
# post_save.connect(clear_cache, sender=Page, dispatch_uid="clear_cache_after_changes")
# post_save.connect(clear_cache, sender=Page_translation, dispatch_uid="clear_cache_after_changes")
#
