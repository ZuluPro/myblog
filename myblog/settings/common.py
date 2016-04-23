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
STATICFILES_DIRS = list(filter(bool, CONFIG.get('DEFAULT', 'staticfiles_dirs').split(',')))
if DEBUG:
    STATICFILES_DIRS += [LOR_STATIC_DIR]
MEDIA_ROOT = CONFIG.get('DEFAULT', 'media_root')
MEDIA_URL = CONFIG.get('DEFAULT', 'media_url')
# STATICFILES_STORAGE = 'lor.storage.LorStorage'
TEST_RUNNER = CONFIG.get('DEFAULT', 'test_runner')
JUXD_FILENAME = CONFIG.get('DEFAULT', 'juxd_filename')
# Flickr
FLICKR_STORAGE_OPTIONS = {
    'api_key': CONFIG.get('DEFAULT', 'flickr_api_key'),
    'api_secret': CONFIG.get('DEFAULT', 'flickr_api_secret'),
    'oauth_token': CONFIG.get('DEFAULT', 'flickr_oauth_token'),
    'oauth_token_secret': CONFIG.get('DEFAULT', 'flickr_oauth_token_secret'),
    'user_id': CONFIG.get('DEFAULT', 'flickr_user_id')
}
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
    'admin_cli',
    'curriculum',
    'curriculum.revealjs',
    'photos',
    'dbbackup',
    'request',
    'favicon',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'request.middleware.RequestMiddleware',
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
    "django.core.context_processors.media",
    "django.core.context_processors.static",
)
if USE_I18N:
    TEMPLATE_CONTEXT_PROCESSORS += (
        'django.core.context_processors.i18n',)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'admin_tools.template_loaders.Loader',
)

if __import__('django').VERSION[1] > 7:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': False,
            'OPTIONS': {
                'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
                'loaders': TEMPLATE_LOADERS,
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
    'pure-grids': ('css/pure-grid.css',
                   'https://cdnjs.cloudflare.com/ajax/libs/pure/0.6.0/grids-responsive-min.css'),
    'angularjs': ('js/angularjs.js',
                  _make_googleapi_url('angularjs/1.3.15/angular.min.js')),
    'wow': ('js/wow.js',
            'https://cdnjs.cloudflare.com/ajax/libs/wow/1.1.2/wow.min.js'),
    'animate': ('css/animate.css',
                'https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.3.0/animate.min.css'),
    'opensans': ('css/opensans.css',
                 'https://fonts.googleapis.com/css?family=Open+Sans:400italic,400,700'),
}

DBBACKUP_STORAGE_OPTIONS = {
    'location': CONFIG.get('DEFAULT', 'backup_dir')
}
FLICKR_CACHE = 'default'

REQUEST_IGNORE_IP = (
    '62.169.67.133',
)
REQUEST_IGNORE_PATHS = (
    r'^admin/',
    r'^/weblog/opensearch\.xml$',
)
REQUEST_IGNORE_USERNAME = (
    'zulu',
)
REQUEST_IGNORE_USER_AGENTS = (
    r'Mozilla/5.0\s*\([^)]*\)\s*AppleWebKit/[0-9.]*\s*\(KHTML, like Gecko\)\s*(Version/[0-9.]*\s*)?\s*Chrome/[0-9.]*\s*(Mobile\s*)?Safari/[0-9.]*',
    r'Googlebot',
    r'Baiduspider',
    r'FeedFetcher',
    r'Mail.RU_Bot',
    r'bingbot',
    r'AhrefsBot',
    r'Netcraft',
    r'SMTBot',
    r'Feedspotbot',
    r'FlipboardProxy',
    r'facebookexternalhit',
    r'LinkedInBot',
    r'Feedfetcher',
)
