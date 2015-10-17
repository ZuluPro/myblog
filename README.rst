===================
My blog source code
===================

.. image:: https://api.travis-ci.org/ZuluPro/myblog.svg
        :target: https://travis-ci.org/ZuluPro/myblog

.. image:: https://coveralls.io/repos/ZuluPro/myblog/badge.svg?branch=master&service=github
        :target: https://coveralls.io/github/ZuluPro/myblog?branch=master
   
.. image:: https://saucelabs.com/browser-matrix/ZuluPro.svg
        :target: https://saucelabs.com/u/ZuluPro
        :alt: Sauce Test Status
        
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
