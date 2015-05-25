import os

from django.conf import settings
from django import template
register = template.Library()


@register.filter(name='emailprotect')
def emailprotect(email):
    filename = os.path.join(settings.STATIC_ROOT, 'themes/' + \
                            settings.MYSMILE_THEME + '/images/email2img.png')
    if os.path.exists(filename):
        return """<img src="/static/themes/""" + \
               settings.MYSMILE_THEME + \
               """/images/email2img.png" alt="email" />"""
    else:
        return '<a href="mailto:' + email + '">' + email + '</a>'
