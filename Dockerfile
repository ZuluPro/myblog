FROM ubuntu
MAINTAINER Anthony MONTHE <anthony.monthe@gmail.com>

ENV PYTHONUNBUFFERED 1
ENV uwsgi_ini /tmp/uwsgi.ini
ENV BLOG_CONFIG_FILE /tmp/myblog.cfg
ENV version master
ENV repo_dir /tmp/myblog-${version}/
ENV app_dir ${repo_dir}/myblog/

ADD extras/docker_uwsgi.ini $uwsgi_ini
ADD extras/docker_compose_myblog.cfg $BLOG_CONFIG_FILE
RUN echo "chdir = $BLOG_CONFIG_FILE" >> $uwsgi_ini

RUN mkdir -p /static/
RUN apt-get update && apt-get install -y \
    build-essential \
    python python-dev python-setuptools \
    libmysqlclient-dev uwsgi
RUN easy_install pip
RUN wget https://github.com/ZuluPro/myblog/archive/master.zip -O- | tar xz -

WORKDIR $repo_dir
RUN pip install -r requirements.txt
RUN python setup.py install
RUN myblog migrate --noinput
RUN myblog collectstatic --noinput

VOLUME /static/

ENTRYPOINT uwsgi
RUN ["--ini", "/tmp/uwsgi.ini"]

EXPOSE 3031
