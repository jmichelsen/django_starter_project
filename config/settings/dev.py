from config.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

try:
    from config.settings.dev_local import *
except ImportError:
    pass
