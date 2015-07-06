#!/bin/bash
set -e

# if command starts with an option, prepend uwsgi
if [ "${1:0:1}" = '-' ]; then
    set -- uwsgi "$@"
fi

if [ -z "$@" ]; then
    set -- uwsgi --ini /uwsgi.ini
fi

echo $@
exec "$@"
