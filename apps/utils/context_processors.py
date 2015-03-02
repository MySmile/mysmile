from django.conf import settings

def mysmile_version(request):
    return {'MYSMILE_VERSION': settings.MYSMILE_VERSION}
