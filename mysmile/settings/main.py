DEBUG = True

if DEBUG:
    from .local import *
else:
    from .production import *

