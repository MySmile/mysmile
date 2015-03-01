from django.contrib import admin

from apps.preferences.models import Preferences
from apps.preferences.forms import PreferencesForm


class PreferencesAdmin(admin.ModelAdmin):
    model = Preferences
    form = PreferencesForm
    fieldsets = [
        ('Preferences', {'fields': ['value', 'description', 'key']}),
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

admin.site.register(Preferences, PreferencesAdmin)
