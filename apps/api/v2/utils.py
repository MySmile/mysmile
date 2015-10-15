import time

from django.conf import settings
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data = {'results': {'code': response.status_code, 'msg': response.data['detail']}}

    return response

#
# class MySmileApiException(Exception):
#
#     def __init__(self, msg, code):
#         self.msg = msg
#         self.code = code
