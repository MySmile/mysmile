from PIL import Image

from django.db import models
from django.db.models import F
from django.http import Http404

import logging
logger = logging.getLogger(__name__)  # Get an instance of a logger

from mysmile.settings.base import LANGUAGES
from apps.preferences.models import Preferences


class ImageField(models.ImageField):

    def save_form_data(self, instance, data):
        if data is not None:
            file = getattr(instance, self.attname)
            if file != data:
                file.delete(save=False)
        super(ImageField, self).save_form_data(instance, data)


def create_default_sortorder():
    return Page.objects.all().aggregate(models.Max('sortorder'))['sortorder__max']+Page.SORTORDER_STEP


class PagesManager(models.Manager):
    def get_content(self, lang=None, slug=None):
        c = self.get_page(lang, slug)
        c['main_menu'] = list(self.get_main_menu(lang))
        return c

    def get_main_menu(self, lang):
        main_menu = Page_translation.objects.filter(lang=lang, page__status=Page.STATUS_PUBLISHED, page__ptype__in=[Page.PTYPE_MENU,Page.PTYPE_MENU_API]).values('page__slug', 'menu').order_by('page__sortorder')
        return main_menu

    def get_page(self, lang, slug):
        try:
            page = Page_translation.objects.filter(lang=lang, page__ptype__in=[Page.PTYPE_INNER, Page.PTYPE_MENU, Page.PTYPE_MENU_API], page__status=Page.STATUS_PUBLISHED, page__slug=slug).values('page__color', 'page__photo', 'menu', 'name', 'col_central', 'col_right', 'youtube', 'col_bottom_1', 'col_bottom_2', 'col_bottom_3', 'photo_alt', 'photo_description', 'meta_title', 'meta_description', 'meta_keywords', 'page__ptype')
        except Exception as err:
            logger.error(err)
            raise Http404

        if page:
            page[0]['bottom_cols'] = list(filter(None, [page[0]['col_bottom_1'], page[0]['col_bottom_2'], page[0]['col_bottom_3']]))
            return page[0]
        else:
            raise Http404


class Page(models.Model):
    PTYPE_INNER = 0
    PTYPE_MENU = 1
    PTYPE_API = 2
    PTYPE_MENU_API = 3
    PTYPE = ((PTYPE_INNER, 'inner page'),  # website only
             (PTYPE_MENU, 'menu page'),  # website only
             (PTYPE_API, 'api page'),   # api only
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
    sortorder = models.IntegerField(unique=True, default=create_default_sortorder, verbose_name='Sort order')
    status = models.IntegerField(unique=False, choices=STATUS, default=STATUS_DRAFT)
    ptype = models.IntegerField(unique=False, choices=PTYPE, default=PTYPE_MENU, verbose_name='Page type')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PagesManager()

    def photo_thumb(self):
        if self.photo:
            description = ''.join(['<img src="', self.photo.url, '" height="32"/> ',
                                     str(round(self.photo.size/1024, 2)), 'K, '
                                    'WxH: ', str(self.photo.width), 'x',
                                    str(self.photo.height), 'px'])

            return description
        else:
            return ''
    photo_thumb.allow_tags = True


    def save(self, *args, **kwargs):
        old_path = self.photo.path if self.photo else None  # save old photo
        super(Page, self).save(*args, **kwargs)  # Call the "real" save() method.
        if self.photo and (self.photo.path != old_path):
            path = self.photo.path
            quality = int(Preferences.objects.filter(key='IMAGE_QUALITY').values_list('value', flat=True)[0])
            image = Image.open(path)
            image.save(path, quality=quality, optimize=True)

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
