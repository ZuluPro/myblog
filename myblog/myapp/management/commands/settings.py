"""
Command for get project settings.
"""
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings as s

DEFAULT_FORMATTERS = (
    'myapp.management.commands._formatters.VersionFormatter',
    'myapp.management.commands._formatters.PythonEnvironmentFormatter',
    'myapp.management.commands._formatters.MainSettingsFormatter',
    'myapp.management.commands._formatters.TestFormatter',
    'myapp.management.commands._formatters.InstalledAppsFormatter',
    'myapp.management.commands._formatters.MiddlewareClassesFormatter',
    'myapp.management.commands._formatters.DatabasesFormatter',
    'myapp.management.commands._formatters.CacheFormatter',
    'myapp.management.commands._formatters.FilesFormatter',
    'myapp.management.commands._formatters.I18nFormatter',
    'myapp.management.commands._formatters.TimeFormatter',
    'myapp.management.commands._formatters.DjangoFormattersFormatter',
    'myapp.management.commands._formatters.TemplateFormatter',
    'myapp.management.commands._formatters.AuthFormatter',
    'myapp.management.commands._formatters.SessionFormatter',
    'myapp.management.commands._formatters.EmailFormatter',
    'myapp.management.commands._formatters.SecurityFormatter',
    'myapp.management.commands._formatters.UrlsFormatter',
    'myapp.management.commands._formatters.LoggingFormatter',
    'myapp.management.commands._formatters.MigrationFormatter',
    'myapp.management.commands._formatters.ModelFormatter',
    'myapp.management.commands._formatters.AdminFormatter',
)


def import_formatter(name):
    splitted_addr = name.split('.')
    module_addr = '.'.join(splitted_addr[:-1])
    object_name = splitted_addr[-1]
    return __import__(module_addr, fromlist=['*'])\
        .__getattribute__(object_name)


def get_formatters():
    fs = []
    for f in s.INSTALLED_APPS:
        try:
            f_module = __import__(f, fromlist=['setting_formatters']).setting_formatters
            for k, v in vars(f_module).items():
                if k.endswith('Formatter'):
                    fs.append('%s.%s' % (v.__module__, v.__name__))
        except AttributeError:
            pass
    return fs


def get_registered_sections():
    return [import_formatter(f)().keyword() for f in get_formatters()]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--ignored', '-i', choices=get_registered_sections(),
            required=False, nargs='*', action='store', dest='ignored',
            default=[], help="Ignore sections")
        parser.add_argument(
            '--only', '-o', choices=get_registered_sections(), required=False,
            nargs='*', action='store', dest='only', default=[],
            help="Only diplay sections")

    def get_used_section(self, opts):
        sections = opts['only'] if opts['only'] else get_registered_sections()
        if opts['ignored']:
            sections = [i for i in sections if not i in opts['ignored']]
        return sections

    def get_used_formatters(self, opts):
        sections = self.get_used_section(opts)
        formatters = [import_formatter(f)() for f in get_formatters()]
        return filter(lambda f: f.keyword() in sections, formatters)

    def handle(self, *args, **opts):
        self.stdout.write('ENV: %s\n' % s.ENV)
        for formatter in self.get_used_formatters(opts):
            self.stdout.write(formatter.get_text())
