import os
from django.contrib import admin
from django.conf import settings

from apps.pages.models import Page, Page_translation
from apps.pages.forms import Page_translationInlineForm, PageForm


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
    max_num = len(settings.LANGUAGES)

    def get_queryset(self, request):
        return Page_translation.objects.filter(lang__in=[x[0] for x in settings.LANGUAGES])

class PageAdmin(admin.ModelAdmin):
    form = PageForm
    inlines = [Page_translationInline]
    save_on_top = True
    readonly_fields = ('photo_thumb',)
    view_on_site = True

    def date_update(self, model):
        return model.updated_at.strftime('%d %B %Y, %H:%M')

    def waiting_for_translation(self, model):
        """ Flag doesn't display if translation prepared
        """
        flags = ''
        for item in settings.LANGUAGES:
            if not Page_translation.objects.filter(page_id=model.id, lang=item[0]):
                flags += """<img src="/static/themes/""" + settings.MYSMILE_THEME + \
                         """/images/flags/""" + item[0] + """.png" alt= " """ + \
                         item[1] + """ "/>"""
        return flags
    waiting_for_translation.short_description = 'waiting for translation'
    waiting_for_translation.allow_tags = True


    def get_list_display(self, request):
        """
        Hide empty colums "photo_thumb" and "waiting_for_translation"
        """
        pages = Page.objects.all().count()
        pages_translation = Page_translation.objects.all().count()
        pages_blankphoto = Page.objects.filter(photo='').count()

        self.list_display = ('slug', 'status', 'ptype', 'sortorder',)

        if pages_blankphoto < pages:  # at least one photo exist
            self.list_display += ('photo_thumb', )
        if pages*len(settings.LANGUAGES) != pages_translation:
            self.list_display += ('waiting_for_translation',)

        return self.list_display + ('date_update',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(PageAdmin, self).get_fieldsets(request, obj)
        if obj:
            photo = Page.objects.filter(id=obj.id).values_list('photo', flat=True)[0]
            if photo:
                fieldsets = [('Settings', {'fields': ['slug', 'status', 'ptype', 'sortorder',
                                                      'color', ('photo', 'photo_thumb')]}), ]
            else:
                fieldsets = [('Settings', {'fields': ['slug', 'status', 'ptype', 'sortorder',
                                                      'color', ('photo',)]}), ]

        return fieldsets


admin.site.register(Page, PageAdmin)

