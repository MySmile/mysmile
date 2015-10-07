import json
import urllib

from django.contrib import messages
from django.views.generic.base import RedirectView
from django.conf import settings

class CheckUpdate(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        try:
            url = 'https://api.github.com/repos/MySmile/mysmile/releases/latest'
            r = urllib.request.urlopen(url)
            latest_release = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
            version = latest_release.get('tag_name')[1::]
            if version > settings.MYSMILE_VERSION:
                msg = 'New version ' + version + ' is avaliable! <a href="' + \
                      latest_release.get('zipball_url') + '"> download now</a>'
            else:
                msg = 'You are up to date!'
        except Exeption as err:
            msg = str(err)

        messages.add_message(self.request, messages.INFO, msg, extra_tags='safe')
        return super(CheckUpdate, self).get_redirect_url(*args, **kwargs)
