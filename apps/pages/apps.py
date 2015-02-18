from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'apps.pages'
    verbose_name = 'Pages'
    label = 'pages'

    def ready(self):
        import apps.pages.signals

