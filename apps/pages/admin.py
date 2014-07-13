import os
from django.contrib import admin

from mysmile.settings.main import MEDIA_URL, STATIC_URL, LANGUAGES
from apps.pages.models import Page, Page_translation, Settings
from apps.pages.forms import Page_translationInlineForm, PageForm, SettingsForm


class Page_translationInline(admin.StackedInline):
    model = Page_translation
    form = Page_translationInlineForm
    verbose_name = 'Lang'
    extra = 0
    fieldsets = [
        ('Content', {'fields': ['lang', 'menu', 'name', 'col_central',
                                'youtube', 'photo_description', 'col_right',
                                'col_bottom_1', 'col_bottom_2', 'col_bottom_3'],
                    'classes': ['collapse']}),
        ('SEO', {'fields': ['meta_title', 'meta_description', 'meta_keywords',
        'photo_alt'], 'classes': ['collapse']}),
    ]
    search_fields = ['col_central', 'col_right', 'col_bottom_1', 'col_bottom_2',
                     'col_bottom_3']
    max_num = len(LANGUAGES)
    

class PageAdmin(admin.ModelAdmin):
    model = Page
    form = PageForm
    fieldsets = [
        ('Settings', {'fields': ['slug', 'status', 'ptype', 'sortorder', 'color', ('photo', 'photo_thumb')]}),
    ]
    inlines = [Page_translationInline]
    list_display = ('slug', 'status', 'ptype', 'sortorder',
                    'photo_thumb', 'waiting_for_translation', 'date_update')
    list_display_links = ('slug',)
    save_on_top = True
    readonly_fields = ('photo_thumb',)

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

class SettingsAdmin(admin.ModelAdmin):
    model = Settings
    form = SettingsForm
    fieldsets = [
        ('Settings', {'fields': ['phone', 'email', 'skype', 'google_code', 'max_inner_link', 'rest_api']}),
    ]
    list_display = ('phone', 'email', 'skype', 'google_code', 'max_inner_link', 'rest_api')
    list_display_links = ('phone', 'email', 'skype', 'google_code', 'max_inner_link', 'rest_api')
    save_on_top = True
    actions = None

    def has_delete_permission(self, request, obj=None):
        """Disable 'delete' button
        """ 
        return False

    def has_add_permission(self, request, obj=None):
        """Disable 'add' button
        """ 
        return False

admin.site.register(Page, PageAdmin)
admin.site.register(Settings, SettingsAdmin)


