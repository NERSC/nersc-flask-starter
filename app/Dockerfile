FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
RUN \
    apt-get update          &&  \
    apt-get --yes upgrade   &&  \
    apt-get --yes install       \
        wget                    \
        bzip2

RUN \
    wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh  &&  \
    bash /tmp/miniconda.sh -f -b -p /opt/miniconda3 &&  \
    rm -rf /tmp/miniconda.sh

ENV PATH /opt/miniconda3/bin:$PATH

RUN \
    conda update --yes conda    &&  \
    conda install --yes             \
        flask                       \
        gunicorn

ADD app.py wsgi.py /opt/app/
ADD templates /opt/app/templates/
RUN ls -laR /opt/app/
