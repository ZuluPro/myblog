"""
Common settings for myblog project.
"""
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
# Email
ADMINS = CONFIG.get('DEFAULT', 'admins').split(',')
EMAIL_BACKEND = CONFIG.get('DEFAULT', 'email_backend')
EMAIL_HOST = CONFIG.get('DEFAULT', 'email_host')
EMAIL_HOST_PASSWORD = CONFIG.get('DEFAULT', 'email_host_password')
EMAIL_HOST_USER = CONFIG.get('DEFAULT', 'email_host_user')
EMAIL_PORT = CONFIG.getint('DEFAULT', 'email_port')
EMAIL_USE_TLS = CONFIG.getboolean('DEFAULT', 'email_use_tls')
EMAIL_USE_SSL = CONFIG.getboolean('DEFAULT', 'email_use_ssl')
# Extra files (CSS, JavaScript, Images)
STATIC_ROOT = CONFIG.get('DEFAULT', 'static_root')
STATIC_URL = CONFIG.get('DEFAULT', 'static_url')
STATICFILES_DIRS = list(filter(bool, CONFIG.get('DEFAULT', 'staticfiles_dirs').split(',')))
MEDIA_ROOT = CONFIG.get('DEFAULT', 'media_root')
MEDIA_URL = CONFIG.get('DEFAULT', 'media_url')
# STATICFILES_STORAGE
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
# Captcha
RECAPTCHA_PUBLIC_KEY = CONFIG.get('DEFAULT', 'recaptcha_public_key')
RECAPTCHA_PRIVATE_KEY = CONFIG.get('DEFAULT', 'recaptcha_private_key')
NOCAPTCHA = CONFIG.getboolean('DEFAULT', 'nocaptcha')
RECAPTCHA_USE_SSL = CONFIG.getboolean('DEFAULT', 'recaptcha_use_ssl')
AKISMET_API_KEY = CONFIG.get('DEFAULT', 'akismet_api_key')

# Application definition
INSTALLED_APPS = (
    'about',
    'django_comments',
    'django_xmlrpc',
    'tinymce',
    'myapp',  # 1st resolved
    'myadmin',
    'mytools',
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
    'request.tracking',
    'favicon',
    'captcha',
    'mycomment',
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
    'mytools.context_processor.tools',
)
if USE_I18N:
    TEMPLATE_CONTEXT_PROCESSORS += (
        'django.core.context_processors.i18n',)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
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

GEOIP_PATH = CONFIG.get('DEFAULT', 'geoip_path')
ZINNIA_SPAM_CHECKER_BACKENDS = (
    'zinnia.spam_checker.backends.long_enough',
    'mycomment.moderator.akismet',
)

DBBACKUP_STORAGE_OPTIONS = {
    'location': CONFIG.get('DEFAULT', 'backup_dir')
}
FLICKR_CACHE = 'default'

REQUEST_IGNORE_IP = (
    '62.169.67.133',
)
REQUEST_IGNORE_PATHS = (
    r'^/$',
    r'^admin/',
    r'^/weblog/opensearch\.xml$',
)
REQUEST_IGNORE_USERNAME = (
    'zulu',
)
REQUEST_IGNORE_USER_AGENTS = (
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
    r'YandexBot',
    r'Yahoo',
)
COMMENTS_APP = 'mycomment'
PROFANITIES_LIST = (
    'bitcoin',
    'protein',
    'minecraft'
)
