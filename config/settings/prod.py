from config.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '.uplynk.com']

try:
    from config.settings.prod_local import *
except ImportError:
    pass
