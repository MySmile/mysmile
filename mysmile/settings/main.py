DEBUG = True

if DEBUG:
    from .local import *
else:
    from .production import *

# load apps settings from apps/someapp/settings.py
for app in LOCAL_APPS:
    try:
        app_module = __import__(app, globals(), locals(), ["settings"])
        app_settings = getattr(app_module, "settings", None)
        for setting in dir(app_settings):
            if setting == setting.upper():
                locals()[setting] = getattr(app_settings, setting)
    except ImportError:
        pass
