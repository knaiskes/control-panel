FROM python:3.7
MAINTAINER Kiriakos Naiskes

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /controlpanel
WORKDIR /controlpanel
COPY ./controlpanel/ /controlpanel
