import traceback
import sys

from django.conf import settings
from django.utils import translation

import logging
logger = logging.getLogger(__name__)


class ExceptionLoggingMiddleware(object):

    def process_exception(self, request, exception):
        logger.error('\n'.join(traceback.format_exception(*sys.exc_info())))


class AdminLocaleOneLangMiddleware:
    """ Autochange locale in admin if len(settings.LANGUAGES) == 1
    """
    def process_request(self, request):
        if len(settings.LANGUAGES) == 1 and request.path.startswith('/admin'):
            translation.activate(settings.LANGUAGES[0][0])
            request.LANGUAGE_CODE = settings.LANGUAGES[0][0]