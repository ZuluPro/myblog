"""
Common settings for myblog project.
"""
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
STATIC_ROOT = CONFIG.get('DEFAULT', 'static_root')
STATIC_URL = CONFIG.get('DEFAULT', 'static_url')
STATICFILES_DIRS = filter(bool, CONFIG.get('DEFAULT', 'staticfiles_dirs').split(','))
MEDIA_ROOT = CONFIG.get('DEFAULT', 'media_root')
MEDIA_URL = CONFIG.get('DEFAULT', 'media_url')
# Application definition
INSTALLED_APPS = (
    'django_comments',
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

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': STATIC_URL + 'admin_tools/js/jquery/jquery.min.js'
}
