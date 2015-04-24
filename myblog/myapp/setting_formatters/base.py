from django.conf import settings as s


class BaseFormatter(object):
    def keyword(self):
        return self.__class__.__name__.replace('Formatter', '').lower()

    def _format_section(self, text, fill='*', align='^'):
        return '\n{0:{fill}{align}79}\n'.format(' %s ' % text, fill=fill, align=align)

    def _format_key_value(self, key, value, fill=' ', align='<'):
        return '{0:{fill}{align}20}: {1}\n'.format(key, value, fill=fill, align=align)

    def get_text(self):
        raise NotImplementedError()


class SettingsFormatter(BaseFormatter):
    def _format_setting(self, name):
        try:
            value = getattr(s, name)
        except AttributeError:
            value = '(Not found)'
        return self._format_key_value(name, value)
