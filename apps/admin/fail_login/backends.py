import datetime
from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from smtplib import SMTPRecipientsRefused

from apps.admin.fail_login.models import FailLogin

import logging
logger = logging.getLogger(__name__)  # Get an instance of a logger


class FailLoginModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        # fail_login injection to django authenticate
        count_fl = self.login_failed(username)
        if count_fl < settings.MYSMILE_ADMIN_FAIL_LOGIN_ATTEMPTS:
            # code below is django authenticate(self, username=None, password=None, **kwargs): ----
            UserModel = get_user_model()
            if username is None:
                username = kwargs.get(UserModel.USERNAME_FIELD)
            try:
                user = UserModel._default_manager.get_by_natural_key(username)
                if user.check_password(password):
                    return user
            except UserModel.DoesNotExist:
                # Run the default password hasher once to reduce the timing
                # difference between an existing and a non-existing user (#20760).
                UserModel().set_password(password)
            # -------------------------------------------------------------------------------------
        else:
            raise PermissionDenied  # 403 error

    def login_failed(self, username):
        try:
            user = User.objects.get(username=username)

            # delete records, older then MYSMILE_ADMIN_FAIL_LOGIN_TIMEOUT
            time = datetime.datetime.now() - timedelta(minutes=settings.MYSMILE_ADMIN_FAIL_LOGIN_TIMEOUT)
            FailLogin.objects.filter(created_at__lte=time).delete()

            count_fl = FailLogin.objects.filter(user=user).count()
            if count_fl < settings.MYSMILE_ADMIN_FAIL_LOGIN_ATTEMPTS:
                FailLogin(user=user).save()
                count_fl += 1
                # Send a one-time email to admin and user about temporary locked account
                if count_fl == settings.MYSMILE_ADMIN_FAIL_LOGIN_ATTEMPTS:
                    # try:
                    subject = '[MySmile] account temporary locked'
                    message = 'You account temporarily locked from '+time.strftime('%Y-%m-%d %H:%M:%S')+' to '+\
                              (time+timedelta(minutes=settings.MYSMILE_ADMIN_FAIL_LOGIN_TIMEOUT)).strftime('%Y-%m-%d %H:%M:%S')
                    try:
                        send_mail(subject, message, settings.SERVER_EMAIL, [settings.ADMINS[0][1]], fail_silently=False)
                    except SMTPRecipientsRefused as ex:
                        logger.error(ex)

                    user_email = User.objects.filter(username=username).values_list('email', flat=True)
                    try:
                        if user_email:
                            send_mail(subject, message, settings.SERVER_EMAIL, user_email, fail_silently=False)
                    except SMTPRecipientsRefused as ex:
                        logger.error(ex)

            else:
                raise PermissionDenied # 403 error
        except ObjectDoesNotExist: # username aren't exist
            logger.info('Attempt to login with username='+username)
        return count_fl