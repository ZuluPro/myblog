import os
from .common import *
from .env import CONFIG

DEBUG = CONFIG.getboolean('DEFAULT', 'debug')
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

# Static
if DEBUG:
    STATICFILES_DIRS = (
    #    os.path.join(BASE_DIR, 'static'),
    )
else:
    STATICFILES_DIRS = ()

if os.environ.get('BLOG_STATIC_ROOT'):
    STATIC_ROOT = os.environ['BLOG_STATIC_ROOT']
elif CONFIG.has_option('DEFAULT', 'static_root') and not CONFIG.get('DEFAULT', 'static_root') is None:
    STATIC_ROOT = CONFIG.get('DEFAULT', 'static_root')
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Media
if os.environ.get('BLOG_MEDIA_ROOT'):
    MEDIA_ROOT = os.environ['BLOG_MEDIA_ROOT']
elif CONFIG.has_option('DEFAULT', 'media_root') and not CONFIG.get('DEFAULT', 'media_root') is None:
    MEDIA_ROOT = CONFIG.get('DEFAULT', 'media_root')
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')
