from django.http import HttpResponsePermanentRedirect
from django.conf import settings

import logging
logger = logging.getLogger(__name__)


class ExceptionLoggingMiddleware(object):

    def process_exception(self, request, exception):
        logger.error('Exception handling request for ' + request.path)
