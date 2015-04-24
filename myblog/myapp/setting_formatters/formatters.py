import sys
import os
import cStringIO
import django
from django.db.models.loading import get_models
from django.core.management import call_command
from django.conf import settings as s
from .base import BaseFormatter, SettingsFormatter

__all__ = [
    'InstalledAppsFormatter',
    'DatabasesFormatter',
    'MiddlewareClassesFormatter',
    'CacheFormatter',
    'FilesFormatter',
    'I18nFormatter',
    'TimeFormatter',
    'DjangoFormattersFormatter',
    'TemplateFormatter',
    'AuthFormatter',
    'SessionFormatter',
    'EmailFormatter',
    'UrlsFormatter',
    'LoggingFormatter',
    'MigrationFormatter',
    'ModelFormatter',
    'SecurityFormatter',
    'AdminFormatter',
    'TestFormatter',
    'VersionFormatter',
    'PythonEnvironmentFormatter',
    'MainSettingsFormatter',
]


class InstalledAppsFormatter(BaseFormatter):
    title = 'INSTALLED_APPS'

    def keyword(self):
        return 'app'

    def _format_app(self, app_name):
        return '{0:30} ({1})\n'.format(app_name, __import__(app_name).__path__[0])

    def get_text(self):
        text = self._format_section(self.title)
        text += '{0:30} {1}\n'.format('APP', 'PACKAGE')
        for a in s.INSTALLED_APPS:
            text += self._format_app(a)
        return text


class DatabasesFormatter(SettingsFormatter):
    title = 'DATABASES'

    def _format_database(self, db_name, conf):
        text = self._format_section(db_name, fill='-')
        for k, v in conf.items():
            if v:
                text += self._format_key_value(k, v)
        return text

    def get_text(self):
        text = self._format_section(self.title)
        self._format_setting('DATABASE_ROUTERS')
        self._format_setting('DEFAULT_INDEX_TABLESPACE')
        self._format_setting('DEFAULT_TABLESPACE')
        for db_name, conf in s.DATABASES.items():
            text += self._format_database(db_name, conf)
        return text


class MiddlewareClassesFormatter(SettingsFormatter):
    title = 'MIDDLEWARE CLASSES'

    def _format_middle(self, middle_addr, debug=False):
        module_name = '.'.join(middle_addr.split('.')[:-2])
        middle_name = middle_addr.split('.')[-1]
        if debug:
            return '{0: <60} {1: >20}\n'.format(middle_addr,
                __import__(module_name, fromlist=[middle_name]).__file__[:-1])
        return '{}\n'.format(middle_addr)

    def get_text(self):
        text = self._format_section(self.title) + '\n'
        for m in s.MIDDLEWARE_CLASSES:
            text += self._format_middle(m)
        return text


class CacheFormatter(SettingsFormatter):
    title = 'CACHES'

    def _format_cache(self, cache_name, conf):
        text = self._format_section(cache_name, fill='-')
        for k, v in conf.items():
            if v:
                text += self._format_key_value(k, v)
        return text

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('USE_ETAGS')
        text += self._format_setting('CACHE_MIDDLEWARE_ALIAS')
        text += self._format_setting('CACHE_MIDDLEWARE_KEY_PREFIX')
        text += self._format_setting('CACHE_MIDDLEWARE_SECONDS')
        for n, c in s.CACHES.items():
            text += self._format_cache(n, c)
        return text


class FilesFormatter(SettingsFormatter):
    title = 'STATIC, MEDIA AND FILES'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('MEDIA_URL')
        text += self._format_setting('MEDIA_ROOT')
        text += self._format_setting('STATIC_URL')
        text += self._format_setting('STATIC_ROOT')
        text += self._format_setting('STATICFILES_STORAGE')
        text += self._format_setting('STATICFILES_DIRS')
        text += self._format_setting('STATICFILES_FINDERS')
        text += self._format_setting('DEFAULT_FILE_STORAGE')
        text += self._format_setting('FILE_CHARSET')
        text += self._format_setting('FILE_UPLOAD_DIRECTORY_PERMISSIONS')
        text += self._format_setting('FILE_UPLOAD_HANDLERS')
        text += self._format_setting('FILE_UPLOAD_MAX_MEMORY_SIZE')
        text += self._format_setting('FILE_UPLOAD_PERMISSIONS')
        text += self._format_setting('FILE_UPLOAD_TEMP_DIR')
        return text


class I18nFormatter(SettingsFormatter):
    title = 'LANGUAGE AND I18N'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('LANGUAGE_CODE')
        text += self._format_setting('USE_I18N')
        text += self._format_setting('USE_L10N')
        text += self._format_setting('LANGUAGE_COOKIE_AGE')
        text += self._format_setting('LANGUAGE_COOKIE_DOMAIN')
        text += self._format_setting('LANGUAGE_COOKIE_NAME')
        text += self._format_setting('LANGUAGE_COOKIE_PATH')
        text += self._format_setting('LOCALE_PATHS')
        text += self._format_setting('LANGUAGES')
        text += self._format_setting('LANGUAGES_BIDI')
        return text


class TimeFormatter(SettingsFormatter):
    title = 'TIME AND DATE'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('TIME_ZONE')
        text += self._format_setting('USE_TZ')
        text += self._format_setting('FIRST_DAY_OF_WEEK')
        return text


class DjangoFormattersFormatter(SettingsFormatter):
    title = 'FORMATTERS'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('TIME_FORMAT')
        text += self._format_setting('TIME_INPUT_FORMATS')
        text += self._format_setting('DATE_FORMAT')
        text += self._format_setting('DATE_INPUT_FORMATS')
        text += self._format_setting('DATETIME_FORMAT')
        text += self._format_setting('DATETIME_INPUT_FORMATS')
        text += self._format_setting('SHORT_DATETIME_FORMAT')
        text += self._format_setting('SHORT_DATE_FORMAT')
        text += self._format_setting('YEAR_MONTH_FORMAT')
        text += self._format_setting('MONTH_DAY_FORMAT')
        text += self._format_setting('DECIMAL_SEPARATOR')
        text += self._format_setting('THOUSAND_SEPARATOR')
        text += self._format_setting('FORMAT_MODULE_PATH')
        text += self._format_setting('NUMBER_GROUPING')
        return text


class TemplateFormatter(SettingsFormatter):
    title = 'TEMPLATE'

    def _format_templates(self):
        text = ''
        for i, conf in enumerate(s.TEMPLATES):
            text += self._format_section(i, fill='-')
            text += self._format_key_value('APP_DIRS', conf['APP_DIRS'])
            text += self._format_key_value('BACKEND', conf['BACKEND'])
            text += self._format_key_value('DIRS', conf['DIRS'])
            text += self._format_key_value('OPTIONS', '')
            for k, v in conf['OPTIONS'].items():
                if v:
                    text += self._format_key_value(k, v)
        return text

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('DEFAULT_CHARSET')
        text += self._format_setting('DEFAULT_CONTENT_TYPE')
        text += self._format_setting('TEMPLATE_DIRS')
        text += self._format_setting('TEMPLATE_LOADERS')
        text += self._format_setting('TEMPLATE_STRING_IF_INVALID')
        text += self._format_setting('TEMPLATE_CONTEXT_PROCESSORS')
        text += self._format_templates()
        return text


class AuthFormatter(SettingsFormatter):
    title = 'AUTHENTICATION'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('AUTH_USER_MODEL')
        text += self._format_setting('AUTHENTICATION_BACKENDS')
        text += self._format_setting('SIGNING_BACKEND')
        text += self._format_setting('AUTH_USER_MODEL')
        text += self._format_setting('LOGIN_REDIRECT_URL')
        text += self._format_setting('LOGIN_URL')
        text += self._format_setting('LOGOUT_URL')
        return text


class SessionFormatter(SettingsFormatter):
    title = 'SESSION'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('SESSION_CACHE_ALIAS')
        text += self._format_setting('SESSION_COOKIE_AGE')
        text += self._format_setting('SESSION_COOKIE_DOMAIN')
        text += self._format_setting('SESSION_COOKIE_HTTPONLY')
        text += self._format_setting('SESSION_COOKIE_NAME')
        text += self._format_setting('SESSION_COOKIE_PATH')
        text += self._format_setting('SESSION_COOKIE_SECURE')
        text += self._format_setting('SESSION_ENGINE')
        text += self._format_setting('SESSION_EXPIRE_AT_BROWSER_CLOSE')
        text += self._format_setting('SESSION_FILE_PATH')
        text += self._format_setting('SESSION_SAVE_EVERY_REQUEST')
        text += self._format_setting('SESSION_SERIALIZER')
        return text


class EmailFormatter(SettingsFormatter):
    title = 'EMAIL'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('SERVER_EMAIL')
        text += self._format_setting('DEFAULT_FROM_EMAIL')
        text += self._format_setting('EMAIL_BACKEND')
        text += self._format_setting('EMAIL_HOST')
        text += self._format_setting('EMAIL_HOST_PASSWORD')
        text += self._format_setting('EMAIL_HOST_USER')
        text += self._format_setting('EMAIL_PORT')
        text += self._format_setting('EMAIL_SSL_CERTFILE')
        text += self._format_setting('EMAIL_SSL_KEYFILE')
        text += self._format_setting('EMAIL_SUBJECT_PREFIX')
        text += self._format_setting('EMAIL_TIMEOUT')
        text += self._format_setting('EMAIL_USE_SSL')
        text += self._format_setting('EMAIL_USE_TLS')
        return text


class UrlsFormatter(SettingsFormatter):
    title = 'URLS'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('SERVER_URL')
        text += self._format_setting('ROOT_URLCONF')
        text += self._format_setting('ABSOLUTE_URL_OVERRIDES')
        text += self._format_setting('APPEND_SLASH')
        text += self._format_setting('PREPEND_WWW')
        return text


class LoggingFormatter(SettingsFormatter):
    title = 'LOGGING'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('LOGGING')
        text += self._format_setting('LOGGING_CONFIG')
        return text


class MigrationFormatter(SettingsFormatter):
    title = 'MIGRATION'

    def _showmigrations(self):
        buf = cStringIO.StringIO()
        call_command('showmigrations', '--list', stdout=buf)
        buf.seek(0)
        return buf.read()

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('MIGRATION_MODULES')
        text += self._showmigrations()
        return text


class ModelFormatter(SettingsFormatter):
    title = 'MODELS'

    def _format_model(self, model):
        return '{0: <30} {1: <20} {2}\n'.format(
            model._meta.app_config.name,
            model.__name__,
            model._meta.db_table,
        )

    def _format_models(self):
        text = '{0: <30} {1:<20} {2}\n'.format('APP', 'MODEL', 'DB TABLE')
        for m in get_models():
            text += self._format_model(m)
        return text

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('FIXTURE_DIRS')
        text += self._format_models()
        return text


class SecurityFormatter(SettingsFormatter):
    title = 'SECURITY'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('SECRET_KEY')
        text += self._format_setting('SECURE_BROWSER_XSS_FILTER')
        text += self._format_setting('SECURE_CONTENT_TYPE_NOSNIFF')
        text += self._format_setting('SECURE_HSTS_INCLUDE_SUBDOMAINS')
        text += self._format_setting('SECURE_HSTS_SECONDS')
        text += self._format_setting('SECURE_PROXY_SSL_HEADER')
        text += self._format_setting('SECURE_REDIRECT_EXEMPT')
        text += self._format_setting('SECURE_SSL_HOST')
        text += self._format_setting('SECURE_SSL_REDIRECT')
        text += self._format_setting('USE_X_FORWARDED_HOST')
        text += self._format_setting('X_FRAME_OPTIONS')
        text += self._format_setting('ALLOWED_HOSTS')
        text += self._format_setting('ALLOWED_INCLUDE_ROOTS')
        text += self._format_setting('PASSWORD_HASHERS')
        text += self._format_setting('PASSWORD_RESET_TIMEOUT_DAYS')
        text += self._format_setting('CSRF_COOKIE_AGE')
        text += self._format_setting('CSRF_COOKIE_DOMAIN')
        text += self._format_setting('CSRF_COOKIE_HTTPONLY')
        text += self._format_setting('CSRF_COOKIE_NAME')
        text += self._format_setting('CSRF_COOKIE_PATH')
        text += self._format_setting('CSRF_COOKIE_SECURE')
        text += self._format_setting('CSRF_FAILURE_VIEW')
        text += self._format_setting('DISALLOWED_USER_AGENTS')
        return text


class AdminFormatter(SettingsFormatter):
    title = 'ADMIN'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('ADMINS')
        return text


class TestFormatter(SettingsFormatter):
    title = 'DEBUG AND TEST'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('DEBUG')
        text += self._format_setting('TEMPLATE_DEBUG')
        text += self._format_setting('DEBUG_PROPAGATE_EXCEPTIONS')
        text += self._format_setting('DEFAULT_EXCEPTION_REPORTER_FILTER')
        text += self._format_setting('IGNORABLE_404_URLS')
        text += self._format_setting('TEST_NON_SERIALIZED_APPS')
        text += self._format_setting('TEST_RUNNER')
        return text


class VersionFormatter(SettingsFormatter):
    title = 'VERSION'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_key_value('Platform', sys.platform)
        text += self._format_key_value('OS Kernel', os.uname()[3])
        text += self._format_key_value('Python executable', sys.executable)
        text += self._format_key_value('Python', sys.version.replace('\n', ''))
        text += self._format_key_value('Django', django.VERSION)
        return text


class PythonEnvironmentFormatter(SettingsFormatter):
    title = 'PYTHON ENVIRONMENT'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_key_value('sys.argv', sys.argv)
        text += self._format_key_value('sys.path', '')
        for p in sys.path:
            text += p + '\n'
        return text


class MainSettingsFormatter(SettingsFormatter):
    title = 'MAIN SETTINGS'

    def get_text(self):
        text = self._format_section(self.title)
        text += self._format_setting('SITE_ID')
        text += self._format_setting('WSGI_APPLICATION')
        text += self._format_setting('BASE_DIR')
        text += self._format_setting('FORCE_SCRIPT_NAME')
        text += self._format_setting('MANAGERS')
        text += self._format_setting('MESSAGE_STORAGE')
        text += self._format_setting('SETTINGS_MODULE')
        text += self._format_setting('SILENCED_SYSTEM_CHECKS')
        return text
