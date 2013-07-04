from django.contrib import admin
from pages.models import Page, Page_translation

from django.db import models
from mysmile import user_settings




class Page_translationInline(admin.StackedInline):#TabularInline):
    model = Page_translation
    extra = 0
    fieldsets = [
        ('Content', {'fields': ['lang','menu','name','central_col','right_col','bottom_col1','bottom_col2','bottom_col3'], 'classes': ['collapse']}),
        ('SEO', {'fields': ['meta_title','meta_description','meta_keywords','photo_alt'],  'classes': ['collapse']}),
    ]
    

class PageAdmin(admin.ModelAdmin):
    model = Page
    fieldsets = [
        (None,               {'fields': ['slug']}),
        ('Main settings', {'fields': ['color','photo','sortorder','status']}),
    ]
    inlines = [Page_translationInline]
    list_display = ('slug',  'status', 'sortorder', 'created_at', 'updated_at')
    list_display_links = ('slug',)#(None,)#
    save_on_top = True
    
    def get_readonly_fields(self, request, obj = None):
        if obj: #In edit mode
            if obj.slug=='index':
                return ('slug',) + self.readonly_fields
        return self.readonly_fields

    # disable 'add' button in condition MAX_NUM_PAGE
    def has_add_permission(self, request):
        num_page = len(Page.objects.filter(status=1))
        if ( num_page >= user_settings.MAX_NUM_PAGE ):
            return False
        else:
            return True
        

admin.site.register(Page, PageAdmin)

