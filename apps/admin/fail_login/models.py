import datetime
from datetime import timedelta

from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class FailLogin(models.Model):
    """ TODO: may be implement IP field?
    """
    # ip = models.IPAddressField(default='0.0.0.0', verbose_name=_('IP'))
    user = models.ForeignKey(User, editable = False, verbose_name=_('User'))
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'FailLogin'
        verbose_name = _('Fail login')
        verbose_name_plural = _('Fail logins')

    # def save(self, *args, **kwargs):
    #     # update timestamps
    #     if not self.id:
    #         self.created_at = timezone.localtime(timezone.now())
    #     # self.modified = datetime.datetime.today()
    #     return super(FailLogin, self).save(*args, **kwargs)

def fl_logged_in(sender, user, request, **kwargs):
    messages.add_message(request, messages.INFO, 'You last login was at '+ str(user.last_login))
    # When a user successfully logs in, delete all "failed_logins" entries for that user
    FailLogin.objects.filter(user=user).delete()

def fl_login_failed(sender, credentials, **kwargs):
    try:
        user = User.objects.get(username=credentials['username'])

        # delete records, older then MYSMILE_ADMIN_LOGIN_TIMEOUT=15min
        time = timezone.localtime(timezone.now()) - timedelta(minutes=settings.MYSMILE_ADMIN_LOGIN_TIMEOUT)
        FailLogin.objects.filter(created_at__gte=time).delete()

        count_fl = FailLogin.objects.filter(user=user).count()
        if count_fl < settings.MYSMILE_ADMIN_LOGIN_ATTEMPTS:
            FailLogin(user=user).save()
        else:
            raise PermissionDenied # 403 error
    except ObjectDoesNotExist: # username aren't exist
        pass


user_logged_in.connect(fl_logged_in)
user_login_failed.connect(fl_login_failed)
