def format_section(text, fill='*'):
    return '\n{0:{fill}{align}79}'.format(' %s ' % text, fill=fill, align='^')


def format_stdout(key, value):
    return '{0:{fill}{align}20}: {1}'.format(key, value, fill=' ', align='<')


def format_app(app_name):
    return '{0:30} ({1})'.format(app_name, __import__(app_name).__path__[0])


def format_middle(middle_addr, debug=False):
    module_name = '.'.join(middle_addr.split('.')[:-2])
    middle_name = middle_addr.split('.')[-1]
    if debug:
        return '{0: <60} {1: >20}'.format(middle_addr,
            __import__(module_name, fromlist=[middle_name]).__file__[:-1])
    return '{}'.format(middle_addr)


def format_database(db_name, conf):
    text = format_section(db_name, fill='-') + '\n'
    for k, v in conf.items():
        if v:
            text += format_stdout(k, v) + '\n'
    return text


def format_cache(cache_name, conf):
    text = format_section(cache_name, fill='-') + '\n'
    for k, v in conf.items():
        if v:
            text += format_stdout(k, v) + '\n'
    return text


def format_dirs(dirs, section=''):
    dirs = [d for d in dirs if d]
    text = format_section(section, fill='-') + '\n' if section else ''
    if not dirs:
        text += 'EMPTY\n'
    for d in dirs:
        if d:
            text += str(d) + '\n'
    return text


def format_templates(full_conf):
    text = ''
    for i, conf in enumerate(full_conf):
        text += format_section(i, fill='-') + '\n'
        text += format_stdout('APP_DIRS', conf['APP_DIRS']) + '\n'
        text += format_stdout('BACKEND', conf['BACKEND']) + '\n'
        text += format_stdout('DIRS', conf['DIRS']) + '\n'
        text += format_stdout('OPTIONS', '') + '\n'
        for k, v in conf['OPTIONS'].items():
            if v:
                text += format_stdout(k, v) + '\n'
    return text


def format_model(model):
    return '{0: <30} {1: <20} {2}'.format(
        model._meta.app_config.name,
        model.__name__,
        model._meta.db_table,
    )
