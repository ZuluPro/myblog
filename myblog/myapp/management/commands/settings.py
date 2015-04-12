"""
Command for get application settings.
"""
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings as s
import django
try:
    import MySQLdb
except ImportError:
    pass
try:
    import django_nose
except ImportError:
    django_nose = None


class Command(BaseCommand):
    def _format_section(self, text):
        return '\n{0:{fill}{align}79}'.format(' %s ' % text, fill='*', align='^')

    def _format_stdout(self, key, value):
        return '{0:{fill}{align}20}: {1}'.format(key, value, fill=' ', align='<')

    def handle(self, *args, **options):
        self.stdout.write(self._format_section('MAIN SETTINGS'))
        self.stdout.write(self._format_stdout('ENV', s.ENV))
        self.stdout.write(self._format_stdout('DEBUG', s.DEBUG))
        self.stdout.write(self._format_stdout('BASE_DIR', s.BASE_DIR))
        self.stdout.write(self._format_stdout('ALLOWED_HOSTS', s.ALLOWED_HOSTS))
        self.stdout.write(self._format_stdout('Django version', django.VERSION))
        # Installed apps
        self.stdout.write(self._format_stdout('INSTALLED_APPS', ''))
        for a in s.INSTALLED_APPS:
            self.stdout.write('    ' + a)
        # Installed Middleware
        self.stdout.write(self._format_stdout('MIDDLEWARE_CLASSES', ''))
        for a in s.MIDDLEWARE_CLASSES:
            self.stdout.write('    ' + a)
        # Database
        self.stdout.write(self._format_section('DATABASES'))
        if s.DATABASES['default']['ENGINE'] == 'django.db.backends.mysql':
            self.stdout.write(self._format_stdout('MySQLdb version', MySQLdb.version_info))
            self.stdout.write(self._format_stdout('USER', s.DATABASES['default']['USER']))
            self.stdout.write(self._format_stdout('NAME', s.DATABASES['default']['NAME']))
            self.stdout.write(self._format_stdout('HOST', s.DATABASES['default']['HOST']))
