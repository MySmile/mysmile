from django.apps import AppConfig


class PreferencesConfig(AppConfig):
    name = 'apps.preferences'
    verbose_name = 'Preferences'
    label = 'preferences'

    def ready(self):
        import apps.preferences.signals
