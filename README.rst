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
        
.. image:: https://ci.solanolabs.com:443/ZuluPro/myblog/badges/branches/master
        :target: https://ci.solanolabs.com:443/ZuluPro/myblog/suites/326373
        :alt: Solano CI build
        
.. image:: https://app.wercker.com/status/dc2d6a378c2ab897009270377575e3da/m/master
        :target: https://app.wercker.com/project/bykey/dc2d6a378c2ab897009270377575e3da
        :alt: Werker build
        
.. image:: https://magnum-ci.com/status/444b783bdfe0d6d2cf46e938963d3c6b.png
        :target: https://magnum-ci.com/projects/3582
        :alt: Magnum CI build

.. image:: https://api.shippable.com/projects/5625d2ab1895ca44741eb548/badge/master
        :target: https://app.shippable.com/projects/5625d2ab1895ca44741eb548
        :alt: Shippable     
        
.. image:: https://coveralls.io/repos/ZuluPro/myblog/badge.svg?branch=master&service=github
        :target: https://coveralls.io/github/ZuluPro/myblog?branch=master
        :alt: Coveralls

.. image:: https://codecov.io/github/ZuluPro/myblog/coverage.svg?branch=master
        :target: https://codecov.io/github/ZuluPro/myblog?branch=master
        :alt: Codercov
        
.. image:: https://codeclimate.com/github/ZuluPro/myblog/badges/gpa.svg
   :target: https://codeclimate.com/github/ZuluPro/myblog
   :alt: Code Climate
   
.. image:: https://api.codacy.com/project/badge/6f22c4f484a645b3ac695dae33b8b724
    :target: https://www.codacy.com/app/anthony-monthe/myblog
    :alt: Codacy health
    
.. image:: https://landscape.io/github/ZuluPro/myblog/master/landscape.svg?style=flat
        :target: https://landscape.io/github/ZuluPro/myblog
        :alt: Landscape IO health
        
.. image:: https://gemnasium.com/ZuluPro/myblog.svg
        :target: https://gemnasium.com/ZuluPro/myblog
        :alt: Gemnasium Dependency
        
.. image:: https://requires.io/github/ZuluPro/myblog/requirements.svg?branch=master
     :target: https://requires.io/github/ZuluPro/myblog/requirements/?branch=master
     :alt: Requirements Status

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
