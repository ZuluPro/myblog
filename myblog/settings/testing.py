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

if TEMPLATE_DEBUG:
    TEMPLATES[0]['OPTIONS']['context_processors']\
        .insert(0, 'django.template.context_processors.debug')

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': STATIC_URL + 'admin_tools/js/jquery/jquery.min.js'
}
