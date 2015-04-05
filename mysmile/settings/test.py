"""
Django settings/test.py for MySmile development project.
"""
import os, sys
import shutil
import tempfile
import logging
logger = logging.getLogger(__name__)  # Get an instance of a logger


from .base import *

# test local
from config.local import *
from .local import *

# test production
# from config.production import *
# from .production import *


class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"


TESTS_IN_PROGRESS = False
if 'test' in sys.argv[1:] or 'jenkins' in sys.argv[1:]:
    logging.disable(logging.CRITICAL)
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )
    DEBUG = False
    TEMPLATE_DEBUG = False
    TESTS_IN_PROGRESS = True
    MIGRATION_MODULES = DisableMigrations()