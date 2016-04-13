from django.db import models
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class FailLogin(models.Model):
    """ Protect admin login from brute-force attack
    """
    user = models.ForeignKey(User, editable = False, verbose_name=_('User'))
    created_at = models.DateTimeField(auto_now_add=True)#(default=datetime.datetime.now())#

    def __unicode__(self):
        return self.user

    class Meta:
        db_table = 'FailLogin'
        verbose_name = _('Fail login')
        verbose_name_plural = _('Fail logins')


def fl_logged_in(sender, user, request, **kwargs):
    # When a user successfully logs in, delete all "failed_logins" entries for that user
    FailLogin.objects.filter(user=user).delete()

user_logged_in.connect(fl_logged_in)
