"""
Testing settings for myblog project.
"""
from .common import *
from .env import CONFIG

SECRET_KEY = '&qaeg(m5s0rpdj-wx@hrc3vpu)v@@n$if67ba-4e9&kk+j$$c+'
# Use Debug toolbar if present
try:
    __import__('imp').find_module('debug_toolbar')
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',)\
        + MIDDLEWARE_CLASSES
    INTERNAL_IPS = CONFIG.get('DEFAULT', 'internal_ips').split(',')
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': CONFIG.get('DEFAULT', 'default_db_engine'),
        'NAME': CONFIG.get('DEFAULT', 'default_db_name'),
        'USER': CONFIG.get('DEFAULT', 'default_db_user'),
        'PASSWORD': CONFIG.get('DEFAULT', 'default_db_password'),
        'HOST': CONFIG.get('DEFAULT', 'default_db_host'),
        'PORT': CONFIG.get('DEFAULT', 'default_db_port'),
    }
}

if __import__('django').VERSION[1] > 7:
    TEMPLATES[0]['OPTIONS']['context_processors'] = \
        ('django.template.context_processors.debug',) + TEMPLATES[0]['OPTIONS']['context_processors']
else:
    TEMPLATES_LOADERS = ('django.template.context_processors.debug',) + TEMPLATES_LOADERS

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': STATIC_URL + 'js/jquery.js'
}
