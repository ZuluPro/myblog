"""
Command for get project settings.
"""
import sys
import os
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.db.models.loading import get_models
from django.conf import settings as s
import django
import _formatters as f

SECTIONS = [
    'main', 'db', 'cache', 'apps', 'middle', 'static', 'i18n', 'time',
    'debug', 'format', 'template', 'session', 'email', 'security',
    'urls', 'logging', 'migrations', 'models', 'version', 'python',
    'auth', 'admin',
]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--ignored', '-i', choices=SECTIONS, required=False, nargs='*',
            action='store', dest='ignored', default=[],
            help="Ignore section")
        parser.add_argument(
            '--only', '-o', choices=SECTIONS, required=False, nargs='*',
            action='store', dest='only', default=[],
            help="Ignore section")

    def get_used_section(self, opts):
        sections = opts['only'] if opts['only'] else SECTIONS
        if opts['ignored']:
            sections = [i for i in sections if not i in opts['ignored']]
        return sections

    def handle(self, *args, **opts):
        sections = self.get_used_section(opts)
        self.stdout.write(f.format_stdout('ENV', s.ENV))
        if 'version' in sections:
            self.stdout.write(f.format_section('VERSION'))
            self.stdout.write(f.format_stdout('Platform', sys.platform))
            self.stdout.write(f.format_stdout('OS Kernel', os.uname()[3]))
            self.stdout.write(f.format_stdout('Python executable', sys.executable))
            self.stdout.write(f.format_stdout('Python', sys.version.replace('\n', '')))
            self.stdout.write(f.format_stdout('Django', django.VERSION))
        if 'python' in sections:
            self.stdout.write(f.format_section('PYTHON ENVIRONMENT'))
            self.stdout.write(f.format_stdout('sys.argv', sys.argv))
            self.stdout.write(f.format_stdout('sys.path', sys.path))
        if 'main' in sections:
            self.stdout.write(f.format_section('MAIN SETTINGS'))
            self.stdout.write(f.format_stdout('SITE_ID', s.SITE_ID))
            self.stdout.write(f.format_stdout('WSGI_APPLICATION', s.WSGI_APPLICATION))
            self.stdout.write(f.format_stdout('BASE_DIR', s.BASE_DIR))
            self.stdout.write(f.format_stdout('FORCE_SCRIPT_NAME', s.FORCE_SCRIPT_NAME))
            self.stdout.write(f.format_stdout('MANAGERS', s.MANAGERS))
            self.stdout.write(f.format_stdout('MESSAGE_STORAGE', s.MESSAGE_STORAGE))
            self.stdout.write(f.format_stdout('SETTINGS_MODULE', s.SETTINGS_MODULE))
            self.stdout.write(f.format_stdout('SILENCED_SYSTEM_CHECKS', s.SILENCED_SYSTEM_CHECKS))
        # Debug
        if 'debug' in sections or 'test' in sections:
            self.stdout.write(f.format_section('DEBUG AND TEST'))
            self.stdout.write(f.format_stdout('DEBUG', s.DEBUG))
            self.stdout.write(f.format_stdout('TEMPLATE_DEBUG', s.TEMPLATE_DEBUG))
            self.stdout.write(f.format_stdout('DEBUG_PROPAGATE_EXCEPTIONS', s.DEBUG_PROPAGATE_EXCEPTIONS))
            self.stdout.write(f.format_stdout('DEFAULT_EXCEPTION_REPORTER_FILTER', s.DEFAULT_EXCEPTION_REPORTER_FILTER))
            self.stdout.write(f.format_stdout('IGNORABLE_404_URLS', s.IGNORABLE_404_URLS))
            self.stdout.write(f.format_stdout('TEST_NON_SERIALIZED_APPS', s.TEST_NON_SERIALIZED_APPS))
            self.stdout.write(f.format_stdout('TEST_RUNNER', s.TEST_RUNNER))
            self.stdout.write(f.format_stdout('DEBUG', s.DEBUG))
        # Apps
        if 'apps' in sections:
            self.stdout.write(f.format_section('INSTALLED_APPS', '-'))
            for a in s.INSTALLED_APPS:
                self.stdout.write(f.format_app(a))
        # Middleware
        if 'middle' in sections:
            self.stdout.write(f.format_section('MIDDLEWARE_CLASSES', '-'))
            for m in s.MIDDLEWARE_CLASSES:
                self.stdout.write(f.format_middle(m))
        # Databases
        if 'db' in sections:
            self.stdout.write(f.format_section('DATABASES'))
            self.stdout.write(f.format_stdout('DATABASE_ROUTERS', s.DATABASE_ROUTERS))
            self.stdout.write(f.format_stdout('DEFAULT_INDEX_TABLESPACE', s.DEFAULT_INDEX_TABLESPACE))
            self.stdout.write(f.format_stdout('DEFAULT_TABLESPACE', s.DEFAULT_TABLESPACE))
            for db_name, conf in s.DATABASES.items():
                self.stdout.write(f.format_database(db_name, conf))
        # Caches
        if s.CACHES and 'cache' in sections:
            self.stdout.write(f.format_section('CACHES'))
            self.stdout.write(f.format_stdout('USE_ETAGS', s.USE_ETAGS))
            self.stdout.write(f.format_stdout('CACHE_MIDDLEWARE_ALIAS', s.CACHE_MIDDLEWARE_ALIAS))
            self.stdout.write(f.format_stdout('CACHE_MIDDLEWARE_KEY_PREFIX', s.CACHE_MIDDLEWARE_KEY_PREFIX))
            self.stdout.write(f.format_stdout('CACHE_MIDDLEWARE_SECONDS', s.CACHE_MIDDLEWARE_SECONDS))
            for cache_name, conf in s.CACHES.items():
                self.stdout.write(f.format_cache(cache_name, conf))
        # Statics
        if 'static' in sections:
            self.stdout.write(f.format_section('STATIC AND MEDIA'))
            self.stdout.write(f.format_stdout('MEDIA_URL', s.MEDIA_URL))
            self.stdout.write(f.format_stdout('MEDIA_ROOT', s.MEDIA_ROOT))
            self.stdout.write(f.format_stdout('STATIC_URL', s.STATIC_URL))
            self.stdout.write(f.format_stdout('STATIC_ROOT', s.STATIC_ROOT))
            self.stdout.write(f.format_stdout('STATICFILES_STORAGE', s.STATICFILES_STORAGE))
            self.stdout.write(f.format_dirs(s.STATICFILES_DIRS, 'STATICFILES_DIRS'))
            self.stdout.write(f.format_dirs(s.STATICFILES_FINDERS, 'STATICFILES_FINDERS'))
            self.stdout.write(f.format_stdout('DEFAULT_FILE_STORAGE', s.DEFAULT_FILE_STORAGE))
            self.stdout.write(f.format_stdout('FILE_CHARSET', s.FILE_CHARSET))
            self.stdout.write(f.format_stdout('FILE_UPLOAD_DIRECTORY_PERMISSIONS', s.FILE_UPLOAD_DIRECTORY_PERMISSIONS))
            self.stdout.write(f.format_stdout('FILE_UPLOAD_HANDLERS', s.FILE_UPLOAD_HANDLERS))
            self.stdout.write(f.format_stdout('FILE_UPLOAD_MAX_MEMORY_SIZE', s.FILE_UPLOAD_MAX_MEMORY_SIZE))
            self.stdout.write(f.format_stdout('FILE_UPLOAD_PERMISSIONS', s.FILE_UPLOAD_PERMISSIONS))
            self.stdout.write(f.format_stdout('FILE_UPLOAD_TEMP_DIR', s.FILE_UPLOAD_TEMP_DIR))
        # Language and i18n
        if 'i18n' in sections:
            self.stdout.write(f.format_section('LANGUAGE AND I18N'))
            self.stdout.write(f.format_stdout('LANGUAGE_CODE', s.LANGUAGE_CODE))
            self.stdout.write(f.format_stdout('USE_I18N', s.USE_I18N))
            self.stdout.write(f.format_stdout('USE_L10N', s.USE_L10N))
            self.stdout.write(f.format_stdout('LANGUAGE_COOKIE_AGE', s.LANGUAGE_COOKIE_AGE))
            self.stdout.write(f.format_stdout('LANGUAGE_COOKIE_DOMAIN', s.LANGUAGE_COOKIE_DOMAIN))
            self.stdout.write(f.format_stdout('LANGUAGE_COOKIE_NAME', s.LANGUAGE_COOKIE_NAME))
            self.stdout.write(f.format_stdout('LANGUAGE_COOKIE_PATH', s.LANGUAGE_COOKIE_PATH))
            self.stdout.write(f.format_stdout('LOCALE_PATHS', s.LOCALE_PATHS))
            self.stdout.write(f.format_dirs(s.LANGUAGES, 'LANGUAGES'))
            self.stdout.write(f.format_dirs(s.LANGUAGES_BIDI, 'LANGUAGES_BIDI'))
        if 'time' in sections:
            self.stdout.write(f.format_section('TIME AND DATE'))
            self.stdout.write(f.format_stdout('TIME_ZONE', s.TIME_ZONE))
            self.stdout.write(f.format_stdout('USE_TZ', s.USE_TZ))
            self.stdout.write(f.format_stdout('FIRST_DAY_OF_WEEK', s.FIRST_DAY_OF_WEEK))
        if 'format' in sections:
            self.stdout.write(f.format_section('FORMATTERS'))
            self.stdout.write(f.format_stdout('TIME_FORMAT', s.TIME_FORMAT))
            self.stdout.write(f.format_stdout('TIME_INPUT_FORMATS', s.TIME_INPUT_FORMATS))
            self.stdout.write(f.format_stdout('DATE_FORMAT', s.DATE_FORMAT))
            self.stdout.write(f.format_stdout('DATE_INPUT_FORMATS', s.DATE_INPUT_FORMATS))
            self.stdout.write(f.format_stdout('DATETIME_FORMAT', s.DATETIME_FORMAT))
            self.stdout.write(f.format_stdout('DATETIME_INPUT_FORMATS', s.DATETIME_INPUT_FORMATS))
            self.stdout.write(f.format_stdout('SHORT_DATETIME_FORMAT', s.SHORT_DATETIME_FORMAT))
            self.stdout.write(f.format_stdout('SHORT_DATE_FORMAT', s.SHORT_DATE_FORMAT))
            self.stdout.write(f.format_stdout('YEAR_MONTH_FORMAT', s.YEAR_MONTH_FORMAT))
            self.stdout.write(f.format_stdout('MONTH_DAY_FORMAT', s.MONTH_DAY_FORMAT))
            self.stdout.write(f.format_stdout('DECIMAL_SEPARATOR', s.DECIMAL_SEPARATOR))
            self.stdout.write(f.format_stdout('THOUSAND_SEPARATOR', s.THOUSAND_SEPARATOR))
            self.stdout.write(f.format_stdout('FORMAT_MODULE_PATH', s.FORMAT_MODULE_PATH))
            self.stdout.write(f.format_stdout('NUMBER_GROUPING', s.NUMBER_GROUPING))
        if 'template' in sections:
            self.stdout.write(f.format_section('TEMPLATE'))
            self.stdout.write(f.format_stdout('DEFAULT_CHARSET', s.DEFAULT_CHARSET))
            self.stdout.write(f.format_stdout('DEFAULT_CONTENT_TYPE', s.DEFAULT_CONTENT_TYPE))
            self.stdout.write(f.format_stdout('TEMPLATE_DIRS', s.TEMPLATE_DIRS))
            self.stdout.write(f.format_stdout('TEMPLATE_LOADERS', s.TEMPLATE_LOADERS))
            self.stdout.write(f.format_stdout('TEMPLATE_STRING_IF_INVALID', s.TEMPLATE_STRING_IF_INVALID))
            self.stdout.write(f.format_dirs(s.TEMPLATE_CONTEXT_PROCESSORS, 'TEMPLATE_CONTEXT_PROCESSORS'))
            self.stdout.write(f.format_templates(s.TEMPLATES))
        if 'auth' in sections:
            self.stdout.write(f.format_section('AUTHENTICATION'))
            self.stdout.write(f.format_stdout('AUTH_USER_MODEL', s.AUTH_USER_MODEL))
            self.stdout.write(f.format_stdout('AUTHENTICATION_BACKENDS', s.AUTHENTICATION_BACKENDS))
            self.stdout.write(f.format_stdout('SIGNING_BACKEND', s.SIGNING_BACKEND))
            self.stdout.write(f.format_stdout('AUTH_USER_MODEL', s.AUTH_USER_MODEL))
            self.stdout.write(f.format_stdout('LOGIN_REDIRECT_URL', s.LOGIN_REDIRECT_URL))
            self.stdout.write(f.format_stdout('LOGIN_URL', s.LOGIN_URL))
            self.stdout.write(f.format_stdout('LOGOUT_URL', s.LOGOUT_URL))
        if 'session' in sections:
            self.stdout.write(f.format_section('SESSION'))
            self.stdout.write(f.format_stdout('SESSION_CACHE_ALIAS', s.SESSION_CACHE_ALIAS))
            self.stdout.write(f.format_stdout('SESSION_COOKIE_AGE', s.SESSION_COOKIE_AGE))
            self.stdout.write(f.format_stdout('SESSION_COOKIE_DOMAIN', s.SESSION_COOKIE_DOMAIN))
            self.stdout.write(f.format_stdout('SESSION_COOKIE_HTTPONLY', s.SESSION_COOKIE_HTTPONLY))
            self.stdout.write(f.format_stdout('SESSION_COOKIE_NAME', s.SESSION_COOKIE_NAME))
            self.stdout.write(f.format_stdout('SESSION_COOKIE_PATH', s.SESSION_COOKIE_PATH))
            self.stdout.write(f.format_stdout('SESSION_COOKIE_SECURE', s.SESSION_COOKIE_SECURE))
            self.stdout.write(f.format_stdout('SESSION_ENGINE', s.SESSION_ENGINE))
            self.stdout.write(f.format_stdout('SESSION_EXPIRE_AT_BROWSER_CLOSE', s.SESSION_EXPIRE_AT_BROWSER_CLOSE))
            self.stdout.write(f.format_stdout('SESSION_FILE_PATH', s.SESSION_FILE_PATH))
            self.stdout.write(f.format_stdout('SESSION_SAVE_EVERY_REQUEST', s.SESSION_SAVE_EVERY_REQUEST))
            self.stdout.write(f.format_stdout('SESSION_SERIALIZER', s.SESSION_SERIALIZER))
        if 'email' in sections:
            self.stdout.write(f.format_section('EMAIL'))
            self.stdout.write(f.format_stdout('SERVER_EMAIL', s.SERVER_EMAIL))
            self.stdout.write(f.format_stdout('DEFAULT_FROM_EMAIL', s.DEFAULT_FROM_EMAIL))
            self.stdout.write(f.format_stdout('EMAIL_BACKEND', s.EMAIL_BACKEND))
            self.stdout.write(f.format_stdout('EMAIL_HOST', s.EMAIL_HOST))
            self.stdout.write(f.format_stdout('EMAIL_HOST_PASSWORD', s.EMAIL_HOST_PASSWORD))
            self.stdout.write(f.format_stdout('EMAIL_HOST_USER', s.EMAIL_HOST_USER))
            self.stdout.write(f.format_stdout('EMAIL_PORT', s.EMAIL_PORT))
            self.stdout.write(f.format_stdout('EMAIL_SSL_CERTFILE', s.EMAIL_SSL_CERTFILE))
            self.stdout.write(f.format_stdout('EMAIL_SSL_KEYFILE', s.EMAIL_SSL_KEYFILE))
            self.stdout.write(f.format_stdout('EMAIL_SUBJECT_PREFIX', s.EMAIL_SUBJECT_PREFIX))
            self.stdout.write(f.format_stdout('EMAIL_TIMEOUT', s.EMAIL_TIMEOUT))
            self.stdout.write(f.format_stdout('EMAIL_USE_SSL', s.EMAIL_USE_SSL))
            self.stdout.write(f.format_stdout('EMAIL_USE_TLS', s.EMAIL_USE_TLS))
        if 'security' in sections:
            self.stdout.write(f.format_section('SECURITY'))
            self.stdout.write(f.format_stdout('SECRET_KEY', s.SECRET_KEY))
            self.stdout.write(f.format_stdout('SECURE_BROWSER_XSS_FILTER', s.SECURE_BROWSER_XSS_FILTER))
            self.stdout.write(f.format_stdout('SECURE_CONTENT_TYPE_NOSNIFF', s.SECURE_CONTENT_TYPE_NOSNIFF))
            self.stdout.write(f.format_stdout('SECURE_HSTS_INCLUDE_SUBDOMAINS', s.SECURE_HSTS_INCLUDE_SUBDOMAINS))
            self.stdout.write(f.format_stdout('SECURE_HSTS_SECONDS', s.SECURE_HSTS_SECONDS))
            self.stdout.write(f.format_stdout('SECURE_PROXY_SSL_HEADER', s.SECURE_PROXY_SSL_HEADER))
            self.stdout.write(f.format_stdout('SECURE_REDIRECT_EXEMPT', s.SECURE_REDIRECT_EXEMPT))
            self.stdout.write(f.format_stdout('SECURE_SSL_HOST', s.SECURE_SSL_HOST))
            self.stdout.write(f.format_stdout('SECURE_SSL_REDIRECT', s.SECURE_SSL_REDIRECT))
            self.stdout.write(f.format_stdout('USE_X_FORWARDED_HOST', s.USE_X_FORWARDED_HOST))
            self.stdout.write(f.format_stdout('X_FRAME_OPTIONS', s.X_FRAME_OPTIONS))
            self.stdout.write(f.format_stdout('ALLOWED_HOSTS', s.ALLOWED_HOSTS))
            self.stdout.write(f.format_stdout('ALLOWED_INCLUDE_ROOTS', s.ALLOWED_INCLUDE_ROOTS))
            self.stdout.write(f.format_stdout('PASSWORD_HASHERS', s.PASSWORD_HASHERS))
            self.stdout.write(f.format_stdout('PASSWORD_RESET_TIMEOUT_DAYS', s.PASSWORD_RESET_TIMEOUT_DAYS))
            self.stdout.write(f.format_stdout('CSRF_COOKIE_AGE', s.CSRF_COOKIE_AGE))
            self.stdout.write(f.format_stdout('CSRF_COOKIE_DOMAIN', s.CSRF_COOKIE_DOMAIN))
            self.stdout.write(f.format_stdout('CSRF_COOKIE_HTTPONLY', s.CSRF_COOKIE_HTTPONLY))
            self.stdout.write(f.format_stdout('CSRF_COOKIE_NAME', s.CSRF_COOKIE_NAME))
            self.stdout.write(f.format_stdout('CSRF_COOKIE_PATH', s.CSRF_COOKIE_PATH))
            self.stdout.write(f.format_stdout('CSRF_COOKIE_SECURE', s.CSRF_COOKIE_SECURE))
            self.stdout.write(f.format_stdout('CSRF_FAILURE_VIEW', s.CSRF_FAILURE_VIEW))
            self.stdout.write(f.format_stdout('DISALLOWED_USER_AGENTS', s.DISALLOWED_USER_AGENTS))
        if 'urls' in sections:
            self.stdout.write(f.format_stdout('SERVER_URL', s.SERVER_URL))
            self.stdout.write(f.format_section('URL AND HTTP'))
            self.stdout.write(f.format_stdout('ROOT_URLCONF', s.ROOT_URLCONF))
            self.stdout.write(f.format_stdout('ABSOLUTE_URL_OVERRIDES', s.ABSOLUTE_URL_OVERRIDES))
            self.stdout.write(f.format_stdout('APPEND_SLASH', s.APPEND_SLASH))
            self.stdout.write(f.format_stdout('PREPEND_WWW', s.PREPEND_WWW))
        if 'logging' in sections:
            self.stdout.write(f.format_section('LOGGING'))
            self.stdout.write(f.format_stdout('LOGGING', s.LOGGING))
            self.stdout.write(f.format_stdout('LOGGING_CONFIG', s.LOGGING_CONFIG))
        if 'migrations' in sections:
            self.stdout.write(f.format_section('MIGRATIONS'))
            self.stdout.write(f.format_stdout('MIGRATION_MODULES', s.MIGRATION_MODULES))
            call_command('showmigrations', '--list')
        if 'models' in sections:
            self.stdout.write(f.format_section('MODELS'))
            self.stdout.write('{0: <30} {1:<20} {2}'.format('APP', 'MODEL', 'DB TABLE'))
            for m in get_models():
                self.stdout.write(f.format_model(m))
            self.stdout.write(f.format_stdout('FIXTURE_DIRS', s.FIXTURE_DIRS))
        if 'admin' in sections:
            self.stdout.write(f.format_section('ADMIN INTERFACE'))
            self.stdout.write(f.format_stdout('ADMINS', s.ADMINS))
