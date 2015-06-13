"""
Common settings for myblog project.
"""
import os
from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS as XMLRPC_METHODS
from .env import CONFIG, BASE_DIR

DEBUG = CONFIG.getboolean('DEFAULT', 'debug')
TEMPLATE_DEBUG = CONFIG.getboolean('DEFAULT', 'template_debug')
ALLOWED_HOSTS = CONFIG.get('DEFAULT', 'allowed_hosts').split(',')
SERVER_URL = CONFIG.get('DEFAULT', 'server_url')
SITE_ID = CONFIG.getint('DEFAULT', 'site_id')
SECRET_KEY = CONFIG.get('DEFAULT', 'secret_key')
ROOT_URLCONF = CONFIG.get('DEFAULT', 'root_urlconf')
WSGI_APPLICATION = CONFIG.get('DEFAULT', 'wsgi_application')
# i18n
LANGUAGE_CODE = CONFIG.get('DEFAULT', 'language_code')
TIME_ZONE = CONFIG.get('DEFAULT', 'time_zone')
USE_I18N = CONFIG.getboolean('DEFAULT', 'use_i18n')
USE_L10N = CONFIG.getboolean('DEFAULT', 'use_l10n')
USE_TZ = CONFIG.getboolean('DEFAULT', 'use_tz')
# Extra files (CSS, JavaScript, Images)
LOR_STATIC_DIR = CONFIG.get('DEFAULT', 'lor_static_dir')
LOR_USE_LOCAL_URLS = CONFIG.getboolean('DEFAULT', 'lor_use_local_urls')
STATIC_ROOT = CONFIG.get('DEFAULT', 'static_root')
STATIC_URL = CONFIG.get('DEFAULT', 'static_url')
STATICFILES_DIRS = filter(bool, CONFIG.get('DEFAULT', 'staticfiles_dirs').split(','))
if DEBUG:
    STATICFILES_DIRS += [LOR_STATIC_DIR]
MEDIA_ROOT = CONFIG.get('DEFAULT', 'media_root')
MEDIA_URL = CONFIG.get('DEFAULT', 'media_url')
# STATICFILES_STORAGE = 'lor.storage.LorStorage'
# Application definition
INSTALLED_APPS = (
    'lor',
    'about',
    'django_comments',
    'django_xmlrpc',
    'tinymce',
    'myapp',  # 1st resolved
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'admin_tools_zinnia',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    'tagging',
    'zinnia',
    'zinnia_tinymce',
    'sorl.thumbnail',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
if __import__('django').VERSION[1] > 7:
    MIDDLEWARE_CLASSES += ('django.middleware.security.SecurityMiddleware',)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'zinnia.context_processors.version',
)
if USE_I18N:
    TEMPLATE_CONTEXT_PROCESSORS += (
        'django.core.context_processors.i18n',)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

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

def _make_googleapi_url(suffix):
    return os.path.join('https://ajax.googleapis.com/ajax/libs/', suffix)

LOR_FILES_URLS = {
    'jquery': ('js/jquery.js',
               _make_googleapi_url('jquery/1.11.3/jquery.min.js')),
    'pure': ('css/pure.css',
             'https://cdnjs.cloudflare.com/ajax/libs/pure/0.6.0/pure.css'),
    'angularjs': ('js/angularjs.js',
                  _make_googleapi_url('angularjs/1.3.15/angular.min.js')),
    'wow': ('js/wow.js',
            'https://cdnjs.cloudflare.com/ajax/libs/wow/1.1.2/wow.min.js'),
    'animate': ('css/animate.css',
                'https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.3.0/animate.min.css'),
    'opensans': ('css/opensans.css',
                 'https://fonts.googleapis.com/css?family=Open+Sans:400italic,400,700'),
}
