import os
from django.contrib import admin

from pages.models import Page, Page_translation
from mysmile.settings import MEDIA_URL, STATIC_URL
from mysmile.settings import LANGUAGES


class Page_translationInline(admin.StackedInline):
    model = Page_translation
    verbose_name = 'Lang'
    extra = 0
    fieldsets = [
        ('Content', {'fields': ['lang', 'menu', 'name', 'central_col',
                                'youtube', 'right_col', 'bottom_col1',
                                'bottom_col2', 'bottom_col3'],
                    'classes': ['collapse']}),
        ('SEO', {'fields': ['meta_title', 'meta_description', 'meta_keywords',
        'photo_alt'], 'classes': ['collapse']}),
    ]
    search_fields = ['central_col', 'right_col', 'bottom_col1', 'bottom_col2',
                     'bottom_col3']
    max_num = len(LANGUAGES)


class PageAdmin(admin.ModelAdmin):
    model = Page
    fieldsets = [
        (None, {'fields': ['slug']}),
        ('Main settings', {'fields': ['color', 'photo', ('sortorder',
                                                         'status', 'ptype')]}),
    ]
    inlines = [Page_translationInline]
    list_display = ('slug', 'status', 'ptype', 'sortorder',
                    'preview_image_url', 'waiting_for_translation',
                    'date_update')
    list_display_links = ('slug',)
    save_on_top = True

    def date_update(self, model):
        return model.updated_at.strftime('%d %B %Y, %H:%M')

    def waiting_for_translation(self, model):
        flags = ''
        for item in LANGUAGES:
            if not Page_translation.objects.filter(page_id=model.id, lang=item[0]):
                flags += '<img src="' + STATIC_URL + \
                         'images/' + item[0] + '.png" alt= "' + str(item[1]) + '"/>'
        return flags
    waiting_for_translation.short_description = 'waiting for translation'
    waiting_for_translation.allow_tags = True

    def preview_image_url(self, model):
        if model.photo:
            image_path = os.path.join(MEDIA_URL, str(model.photo))
            return '<img src="' + image_path + '" height="32"/>'
        else:
            return ''

    preview_image_url.short_description = 'Thumbnails'
    preview_image_url.allow_tags = True

admin.site.register(Page, PageAdmin)
