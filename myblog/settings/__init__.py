from __future__ import absolute_import
import sys
from .env import ENV

if 'test' in sys.argv or ENV == 'ci':
    from .test import *
elif ENV == 'prod':
    from .prod import *
elif ENV == 'preprod':
    from .preprod import *
elif ENV == 'testing':
    from .testing import *
else:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured('Set environment in env.py file.')
