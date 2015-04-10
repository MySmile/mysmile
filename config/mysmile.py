# MySmile settings
from django.conf import settings

MYSMILE_VERSION='0.6.2'

# for MYSMILE_VERSION availability in templates
TEMPLATE_CONTEXT_PROCESSORS = settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'apps.utils.context_processors.mysmile_version',
)