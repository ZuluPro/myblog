My Docker-Compose manual
========================

Instructions
------------

1. ``cd`` to root of this repo
2. ``cp extras/docker-compose/compose.env{.example,}``
3. Edit ``extras/docker-compose/compose.env`` for contains great variables
4. Add your certificate, key and DH cert in ``extras/docker-compose/ssl-certs/``.
   Name them as following:
   - myblog.crt
   - myblog.key
   - dhparam.pem
5. Launch with ``docker-compose up``
