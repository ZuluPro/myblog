"""
Dynamic settings module made for set a :class:`ConfigParser.SafeConfigParser`
with all parameters from configuration file, environment variables and
parser's default values.
"""
import os
try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser

# Base path of project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Get env vars
ENV_VARS = {
    k.replace('BLOG_', '').lower(): v
    for k, v in os.environ.items()
    if k.startswith('BLOG_')
}
# Set default values
DEFAULT_CONFIG = {
    'env': 'prod',
    'debug': 'False',
    'template_debug': 'False',
    'server_url': 'anthony.monthe.me',
    'site_id': '1',
    'allowed_hosts': '*',
    'secret_key': None,
    'root_urlconf': 'urls',
    'wsgi_application': 'wsgi.application',
    'session_engine': 'django.contrib.sessions.backends.cached_db',
    # Database
    'default_db_engine': 'django.db.backends.sqlite3',
    'default_db_name': os.path.join(BASE_DIR, 'db.sqlite3'),
    'default_db_user': '',
    'default_db_password': '',
    'default_db_host': '',
    'default_db_port': '',
    # Email
    'admins': '',
    'email_backend': 'django.core.mail.backends.smtp.EmailBackend',
    'email_host': 'localhost',
    'email_host_password': '',
    'email_host_user': '',
    'email_port': '25',
    'email_use_tls': 'False',
    'email_use_ssl': 'False',
    # Misc
    'geoip_path': '/usr/local/share/GeoIP/',
    # Extra files
    'lor_use_local_urls': 'False',
    'lor_static_dir': '/tmp/lor/',
    'static_root': os.path.join(BASE_DIR, 'static/'),
    'media_root': os.path.join(BASE_DIR, 'media/'),
    'static_url': '/static/',
    'media_url': '/uploads/',
    'staticfiles_dirs': '',
    'backup_dir': os.path.expanduser('~'),
    # i18n
    'language_code': 'en-us',
    'time_zone': 'UTC',
    'use_i18n': 'False',
    'use_l10n': 'False',
    'use_tz': 'False',
    # Cache
    'cache_backend': 'redis_cache.cache.RedisCache',
    'cache_location': '127.0.0.1:6379:1',
    'cache_option_client_class': 'redis_cache.client.DefaultClient',
    # Test
    'test_runner': 'django.test.runner.DiscoverRunner',
    'internal_ips': '127.0.0.1',
    'juxd_filename': os.path.join(BASE_DIR, 'junit.xml'),
    # Flickr
    'flickr_api_key': None,
    'flickr_api_secret': None,
    'flickr_oauth_token': None,
    'flickr_oauth_token_secret': None,
    'flickr_user_id': None,
    # Captcha
    'recaptcha_public_key': None,
    'recaptcha_private_key': None,
    'nocaptcha': 'True',
    'recaptcha_use_ssl': 'True',
    'akismet_api_key': None,
}
# Choose conf file to read
CONFIG_FILE = os.environ.get('BLOG_CONFIG_FILE',
                             os.path.join(os.getcwd(), '.myblog.cfg'))
# Read it
CONFIG = SafeConfigParser(defaults=DEFAULT_CONFIG, allow_no_value=True)
CONFIG.read([
    CONFIG_FILE,
    '/etc/myblog.cfg',
    os.path.expanduser('~/.myblog.cfg')
])
map(lambda i: CONFIG.set('DEFAULT', i[0], i[1]),
    ENV_VARS.items())
# Set ENV shortcut var
ENV = CONFIG.get('DEFAULT', 'env')
