import json
import urllib

from django.contrib import messages
from django.views.generic.base import RedirectView
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class CheckUpdate(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        try:
            url = 'https://api.github.com/repos/MySmile/mysmile/releases/latest'
            r = urllib.request.urlopen(url)
            latest_release = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
            version = latest_release.get('tag_name')[1::]
            if version > settings.MYSMILE_VERSION:
                msg = _('New version ') + version + _(' is avaliable!') + '<a href="' +\
                      latest_release.get('zipball_url') + '">' + _(' download now') + '</a>'
            else:
                msg = _('You are up to date!')
        except Exeption as err:
            msg = str(err)

        messages.add_message(self.request, messages.INFO, msg, extra_tags='safe')
        return super(CheckUpdate, self).get_redirect_url(*args, **kwargs)
