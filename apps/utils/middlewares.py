from django.http import HttpResponsePermanentRedirect
from django.conf import settings
from django.utils import translation

import logging
logger = logging.getLogger(__name__)


class ExceptionLoggingMiddleware(object):

    def process_exception(self, request, exception):
        logger.error('Exception handling request for ' + request.path)


class AdminLocaleOneLangMiddleware:
    """ Autochange locale in admin if len(settings.LANGUAGES) == 1
    """
    def process_request(self, request):
        if request.path.startswith('/admin') and len(settings.LANGUAGES) == 1:
            translation.activate(settings.LANGUAGES[0][0])
            request.LANGUAGE_CODE = settings.LANGUAGES[0][0]