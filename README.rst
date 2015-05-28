===================
My blog source code
===================


Installation
============

Ansible
=======

An ansible install in foundable at `/extras/ansible/README.rst`_.

.. _/extras/ansible/README.rst: /extras/ansible/README.rst

Manual install
==============

Make a simple package installation:

.. code::

    pip install -r requirements.txt
    python setup.py install
    cp extras/myblog.cfg.example /etc/myblog.cfg

Most settings in ``myblog.cfg`` have a default value, for example default
database is Sqlite stored at ``myblog/db.sqlite3``.

Tests
=====

``./manage test``
