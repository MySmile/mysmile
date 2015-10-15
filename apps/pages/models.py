from django.db import models
from django.http import Http404
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)  # Get an instance of a logger

from django.conf import settings


class ImageField(models.ImageField):

    def save_form_data(self, instance, data):
        if data is not None:
            file = getattr(instance, self.attname)
            if file != data:
                file.delete(save=False)
        super(ImageField, self).save_form_data(instance, data)

def create_default_sortorder():
    default_sortorder = Page.objects.all().aggregate(models.Max('sortorder'))['sortorder__max']
    default_sortorder = default_sortorder + Page.SORTORDER_STEP if default_sortorder else Page.SORTORDER_STEP
    return default_sortorder

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
    PTYPE = ((PTYPE_INNER, _('inner page')),  # website only
             (PTYPE_MENU, _('menu page')),  # website only
             (PTYPE_API, _('API page')),   # API only
             (PTYPE_MENU_API, _('API & menu page')))  # API & website

    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1
    STATUS = ((STATUS_DRAFT, _('draft')),
              (STATUS_PUBLISHED, _('published')))
    SORTORDER_STEP = 10

    slug = models.SlugField(unique=True, verbose_name=_('slug'))
    color = models.CharField(max_length=255, default='#FDA132',
                             help_text=_('Click once with the mouse to select \
                                        a color, and then twice to save. TEMPORARY DISABLED IN NON-CLASSIC THEMES!'),
                             verbose_name=_('color'))
    # blank=True add "clear image" checkbox into admin page
    photo = ImageField(upload_to='images/', null=True, blank=True, verbose_name=_('photo'))
    sortorder = models.IntegerField(unique=True, default=create_default_sortorder, verbose_name=_('Sort order'))
    status = models.IntegerField(unique=False, choices=STATUS, default=STATUS_DRAFT, verbose_name=_('status'))
    ptype = models.IntegerField(unique=False, choices=PTYPE, default=PTYPE_MENU, verbose_name=_('page type'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PagesManager()

    def photo_thumb(self):
        if self.photo:
            try:
                description = ''.join(['<img src="', self.photo.url, '" height="32"/> ',
                                     str(round(self.photo.size/1024, 2)), 'K, '
                                    'WxH: ', str(self.photo.width), 'x',
                                    str(self.photo.height), 'px'])
            except FileNotFoundError:
                return ''
            return description
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
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')

class Page_translation(models.Model):
    page = models.ForeignKey(Page)
    lang = models.CharField(max_length=255, choices=settings.LANGUAGES,
                            default=settings.LANGUAGES[0][0], verbose_name=_('lang'))
    menu = models.CharField(max_length=255, verbose_name=_('menu'))
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('name'))
    col_central = models.TextField(blank=False, null=False, verbose_name=_('central column'))
    youtube = models.CharField(max_length=255, blank=True, null=True,
                               help_text=_('Link to youtube video. \
                               Max length url =  2048 characters'), verbose_name=_('youtube'))
    col_right = models.TextField(blank=True, null=True, verbose_name=_('right column'))
    col_bottom_1 = models.TextField(blank=True, null=True, verbose_name=_('bottom column 1'))
    col_bottom_2 = models.TextField(blank=True, null=True, verbose_name=_('bottom column 2'))
    col_bottom_3 = models.TextField(blank=True, null=True, verbose_name=_('bottom column 3'))

    meta_title = models.CharField(max_length=255, verbose_name=_('meta title'))
    meta_description = models.CharField(max_length=255, verbose_name=_('meta description'))
    meta_keywords = models.CharField(max_length=255, verbose_name=_('meta keywords'))
    photo_alt = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('photo alt'))
    photo_description = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('photo description'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __unicode__(self):
        return self.lang

    class Meta:
        db_table = 'Page_translation'
        ordering = ['lang']
        verbose_name = _('Translation')
        verbose_name_plural = _('Translations')
        unique_together = ('page', 'lang')

    def get_absolute_url(self):
        return reverse('page', kwargs={'lang': self.lang, 'slug': self.page.slug})
