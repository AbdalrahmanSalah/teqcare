FROM python:3.11.0a3-alpine


ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /TEQCare
WORKDIR /TEQCare
COPY ./TEQCare /TEQCare

RUN adduser -D user
USER user
