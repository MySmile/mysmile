from django.conf import settings


def mysmile_version(request):
    return {'MYSMILE_VERSION': settings.MYSMILE_VERSION}

def mysmile_theme(request):
    return {'MYSMILE_THEME': settings.MYSMILE_THEME}
