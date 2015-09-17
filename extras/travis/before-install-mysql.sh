#!/bin/bash
PYTHON_VERSION=$(python -c 'import sys; print(sys.version_info[0])')

if [[ "$PYTHON_VERSION" == 2 ]]
then pip install mysql-python
else pip install PyMySQL
fi
mysql -e 'CREATE DATABASE IF NOT EXISTS myblog;'
mysql -e "SET GLOBAL wait_timeout=28800;"
