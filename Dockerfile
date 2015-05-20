FROM python:2
MAINTAINER Anthony MONTHE <anthony.monthe@gmail.com>

ENV PYTHONUNBUFFERED 1
ENV uwsgi_ini /tmp/uwsgi.ini
ENV BLOG_CONFIG_FILE /tmp/myblog.cfg
ENV version docker
ENV repo_dir /src/myblog
ENV app_dir ${repo_dir}/myblog/

ADD . $repo_dir
ADD extras/docker/uwsgi.ini $uwsgi_ini
ADD extras/docker/myblog.cfg $BLOG_CONFIG_FILE
ADD extras/docker-entrypoint.sh /docker-entrypoint.sh
RUN echo "chdir = $app_dir" >> $uwsgi_ini

WORKDIR $repo_dir
RUN pip install -r requirements.txt
RUN pip install MySQL-Python uwsgi
RUN python setup.py install
# RUN myblog collectstatic --noinput

VOLUME /static

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["uwsgi", "--ini", "/tmp/uwsgi.ini"]

EXPOSE 3031
