from django.contrib import admin
from django.db import models
#~ from django.forms import Textarea
from django.db import connection

from pages.models import Page, Page_translation
from mysmile.user_settings import user_settings


class Page_translationInline(admin.StackedInline):  # TabularInline):
    model = Page_translation
    # model.lang.help_text('SOME HELP!')
    extra = 0
    fieldsets = [
        ('Content', {'fields': ['lang', 'menu', 'name', 'central_col', 'youtube', 'right_col', 
        'bottom_col1', 'bottom_col2', 'bottom_col3'], 'classes': ['collapse']}),
        ('SEO', {'fields': ['meta_title', 'meta_description', 'meta_keywords', 
        'photo_alt'], 'classes': ['collapse']}),
    ]
    search_fields = ['central_col', 'right_col', 'bottom_col1', 'bottom_col2', 'bottom_col3']
    max_num = len(user_settings['ALL_LANGS'])

class PageAdmin(admin.ModelAdmin):
    model = Page
    fieldsets = [
        (None, {'fields': ['slug']}),
        ('Main settings', {'fields': ['color',('photo','add_img'),('sortorder','status','ptype')]}),
    ]
    inlines = [Page_translationInline]
    list_display = ('slug', 'status', 'ptype', 'sortorder', 'created_at', 'updated_at')
    list_display_links = ('slug',)
    save_on_top = True
    readonly_fields = ('add_img',) 
    #~ def get_readonly_fields(self, request, obj=None):
        #~ if obj:  # In edit mode
            #~ if obj.slug == 'index':
                #~ return ('slug',) + self.readonly_fields
        #~ return self.readonly_fields

admin.site.register(Page, PageAdmin)

