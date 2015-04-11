import os
from ConfigParser import SafeConfigParser


CONFIG_FILE = os.environ.get('BLOG_CONFIG_FILE', '/etc/myblog')
CONFIG = SafeConfigParser(defaults={
    'env': 'prod',
    'debug': 'False',
    'server_url': 'anthony.monthe.me',
    # Cache
    'cache_backend': 'redis_cache.cache.RedisCache',
    'cache_location': '127.0.0.1:6379:1',
    'cache_option_client_class': 'redis_cache.client.DefaultClient',

}, allow_no_value=True)
CONFIG.read(CONFIG_FILE)


ENV = os.environ.get('BLOG_ENV') or CONFIG.get('DEFAULT', 'env')
DEBUG = CONFIG.getboolean('DEFAULT', 'debug')
SERVER_URL = CONFIG.get('DEFAULT', 'server_url')

CACHES = {
    'default': {
        'BACKEND': CONFIG.get('DEFAULT', 'cache_backend'),
        'LOCATION': CONFIG.get('DEFAULT', 'cache_location'),
        'OPTIONS': {
            'CLIENT_CLASS': CONFIG.get('DEFAULT', 'cache_option_client_class'),
            'SOCKET_TIMEOUT': 5,
            # 'PASSWORD': ''
        }
    }
}
