import os
from .common import *
from .env import CONFIG

TEMPLATE_DEBUG = True

SECRET_KEY = '&qaeg(m5s0rpdj-wx@hrc3vpu)v@@n$if67ba-4e9&kk+j$$c+'

# Debug toolbar
try:
    __import__('imp').find_module('debug_toolbar')
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE_CLASSES
    INTERNAL_IPS = (
        '127.0.0.1',
    )
except ImportError:
        pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
