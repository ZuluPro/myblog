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

.. image:: https://drone.io/github.com/ZuluPro/myblog/status.png
        :target: https://drone.io/github.com/ZuluPro/myblog
        :alt: Drone IO build

.. image:: https://codeship.com/projects/7602bb80-5c6c-0133-ab8c-1a7f023b972a/status?branch=master
        :target: https://codeship.com/projects/110945
        :alt: Codeship test

.. image:: https://ci.appveyor.com/api/projects/status/nsua6i3lx50qv57o?svg=true
        :target: https://ci.appveyor.com/project/ZuluPro/myblog
        :alt: Appveyor build
        
.. image:: https://ci.solanolabs.com/ZuluPro/myblog/badges/branches/master?badge_token=f7f64514d931c3eb5b4e1c59e54f9ac9c951f016

        :target: https://ci.solanolabs.com/ZuluPro/myblog/
        :alt: Solano CI build

.. image:: https://coveralls.io/repos/ZuluPro/myblog/badge.svg?branch=master&service=github
        :target: https://coveralls.io/github/ZuluPro/myblog?branch=master
        :alt: Coveralls
        
.. image:: https://codeclimate.com/github/ZuluPro/myblog/badges/gpa.svg
   :target: https://codeclimate.com/github/ZuluPro/myblog
   :alt: Code Climate
      
.. image:: https://landscape.io/github/ZuluPro/myblog/master/landscape.svg?style=flat
        :target: https://landscape.io/github/ZuluPro/myblog
        :alt: Landscape IO health
        
.. image:: https://gemnasium.com/ZuluPro/myblog.svg
        :target: https://gemnasium.com/ZuluPro/myblog
        :alt: Gemnasium Dependency

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
