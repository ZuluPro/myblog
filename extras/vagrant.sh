#!/usr/bin/env bash

set -e

PROJECT_NAME=myblog
PROJECT_DIR=/home/vagrant/$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/venv
MYBLOG_CONFIG_FILE=/etc/myblog.cfg


install_myblog_packages () {
    apt-get update -y
    apt-get install -y gcc python python-dev python-setuptools
    easy_install pip
}

install_venv () {
    pip install virtualenv
    su - vagrant -c "/usr/local/bin/virtualenv $VIRTUALENV_DIR"
}

install_myblog () {
    cp $PROJECT_DIR/extras/myblog.cfg.vagrant $MYBLOG_CONFIG_FILE
    chown vagrant: $MYBLOG_CONFIG_FILE
    chmod 600 $MYBLOG_CONFIG_FILE

    su - vagrant -c " \
        cd $PROJECT_DIR && \
        $VIRTUALENV_DIR/bin/pip install -r requirements.txt && \
        $VIRTUALENV_DIR/bin/python myblog/manage.py migrate --noinput"
}

main () {
    install_myblog_packages
    install_venv
    install_myblog
}

main
