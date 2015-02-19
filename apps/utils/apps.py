from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = 'apps.utils'
    verbose_name = 'Utils'
    label = 'utils'

    def ready(self):
        import apps.utils.signals
