import logging

from config.settings.base import *

DEBUG = True

logging.disable(logging.CRITICAL)

try:
    from config.settings.test_local import *
except ImportError:
    pass
