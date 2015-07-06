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
    # Extra files
    'lor_use_local_urls': 'False',
    'lor_static_dir': '/tmp/lor/',
    'static_root': os.path.join(BASE_DIR, 'static/'),
    'media_root': os.path.join(BASE_DIR, 'media/'),
    'static_url': '/static/',
    'media_url': '/uploads/',
    'staticfiles_dirs': '',
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
    'internal_ips': '127.0.0.1',
}
# Choose conf file to read
CONFIG_FILE = os.environ.get('BLOG_CONFIG_FILE', '/etc/myblog.cfg')
# Read it
CONFIG = SafeConfigParser(defaults=DEFAULT_CONFIG, allow_no_value=True)
CONFIG.read(CONFIG_FILE)
map(lambda i: CONFIG.set('DEFAULT', i[0], i[1]),
    ENV_VARS.items())
# Set ENV shortcut var
ENV = CONFIG.get('DEFAULT', 'env')
