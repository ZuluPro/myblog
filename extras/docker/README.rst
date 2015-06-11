My Docker manual
================

How it works
------------

Requirements
************

- An host with docker installed and available

Instructions
------------

From repo's root:

#. Build image ``docker build .``
#. Launch a container with image: ``docker run myblog uwsgi --ini /tmp/uwsgi.ini``

.. image:: ../docs/_static/know_docker.jpg
