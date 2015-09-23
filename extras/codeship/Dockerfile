FROM python:2
MAINTAINER Anthony MONTHE <anthony.monthe@gmail.com>

ENV PYTHONUNBUFFERED 1
ENV repo_dir /src/myblog
ENV app_dir ${repo_dir}/myblog/

ADD . $repo_dir

WORKDIR $repo_dir

RUN pip install -r requirements.txt requirements-tests.txt
RUN python setup.py install
