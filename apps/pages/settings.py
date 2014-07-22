from apps.pages.models import Settings


app_settings = Settings.objects.filter(key__in = ['PHONE', 'EMAIL', 'SKYPE', 'GOOGLE_ANALITYCS_CODE', 'MAX_INNERLINK_HISTORY']).values('key','value')
APP_SETTINGS = {}
for item in app_settings:
    APP_SETTINGS.update({item['key']:item['value']})

