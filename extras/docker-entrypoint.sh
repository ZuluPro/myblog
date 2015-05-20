#!/bin/bash
set -e

# if command starts with an option, prepend uwsgi
if [ "${1:0:1}" = '-' ]; then
    set -- uwsgi "$@"
fi

if [ -z "$@" ]; then
    set -- uwsgi --ini /tmp/uwsgi.ini
fi

echo 1 $@ 2
exec "$@"
