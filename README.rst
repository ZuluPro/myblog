===================
My blog source code
===================

.. image:: https://circleci.com/gh/ZuluPro/myblog/tree/master.svg?style=shield
        :target: https://circleci.com/gh/ZuluPro/myblog
        :alt: CircleCI build

.. image:: https://api.travis-ci.org/ZuluPro/myblog.svg
        :target: https://travis-ci.org/ZuluPro/myblog
        :alt: Travis build
        
.. image:: https://snap-ci.com/ZuluPro/myblog/branch/master/build_image
        :target: https://snap-ci.com/ZuluPro/myblog/branch/master
        :alt: Snap-CI build

.. image:: https://semaphoreci.com/api/v1/projects/7874fd94-37b8-4aa3-a70a-1314890c8ee1/574928/badge.svg
        :target: https://semaphoreci.com/zulupro/myblog/branches/master
        :alt: Semaphore CI build

.. image:: https://coveralls.io/repos/ZuluPro/myblog/badge.svg?branch=master&service=github
        :target: https://coveralls.io/github/ZuluPro/myblog?branch=master
        :alt: Coveralls
        
.. image:: https://codeclimate.com/github/ZuluPro/myblog/badges/gpa.svg
   :target: https://codeclimate.com/github/ZuluPro/myblog
   :alt: Code Climate
   
.. image:: https://saucelabs.com/browser-matrix/ZuluPro.svg
        :target: https://saucelabs.com/u/ZuluPro
        :alt: Sauce Test Status
        
https://semaphoreci.com/api/v1/projects/7874fd94-37b8-4aa3-a70a-1314890c8ee1/574928/badge.svg
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
