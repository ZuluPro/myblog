"""This file import settings variable from appropriate file."""
from __future__ import absolute_import
from .env import ENV

if ENV == 'prod':
    from .prod import *
elif ENV == 'testing':
    from .testing import *
else:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured('Please, set environment on "prod" or "testing".')
