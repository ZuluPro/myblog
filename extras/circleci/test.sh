#!/bin/bash
# Shortcut for launch command with CircleCI in specified virtualenv/job
# $1 - Command to launch

CMD[0]='tox -e py2.7-django1.7-sqlite'
CMD[1]='tox -e py2.7-django1.8-sqlite'
CMD[2]='tox -e py2.7-django1.7-mysql'
CMD[3]='tox -e py2.7-django1.8-mysql'

TOX_CMD="${CMD[${CIRCLE_NODE_INDEX}]}"
case $TOX_CMD in
    *-*-mysql)
        cp extras/circleci/myblog-mysql.cfg ~/.myblog.cfg
        mysql -e "SET GLOBAL wait_timeout=28800;"
        mysql -e "SET GLOBAL storage_engine=MyISAM;"
esac

${TOX_CMD} $@
