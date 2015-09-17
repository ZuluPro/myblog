#!/bin/bash
mkdir -p /tmp/static/ /tmp/media/ /tmp/lor
myblog/manage.py collectstatic --noinput
