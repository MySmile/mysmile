from django.contrib import admin
from django.db.models.signals import post_save
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from apps.settings.models import Settings
from apps.settings.forms import SettingsForm


class SettingsAdmin(admin.ModelAdmin):
    model = Settings
    form = SettingsForm
    fieldsets = [
        ('Settings', {'fields': ['value', 'description', 'key']}),
    ]
    list_display = ('name', 'value')
    list_display_links = ('name',)
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

def clear_cach(sender, instance, **kwargs):
    """Clear cache after save in admin
    """
    key = make_template_fragment_key('block_contact')
    cache.delete(key)
    cache.delete('app_settings')

post_save.connect(clear_cach, sender=Settings, dispatch_uid="clear_cach_from_admin")
admin.site.register(Settings, SettingsAdmin)
