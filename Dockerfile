# syntax=docker/dockerfile:1
FROM python:3.11-alpine3.17
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/

# Installing client libraries and any other package you need
RUN apk update && apk add libpq

RUN apk update \
  # dependencies for building Python packages
  && apk install build-essential \
  # psycopg2 dependencies
  && apk install libpq-dev

RUN pip install -r requirements.txt

# Delete build dependencies
RUN apk del .build-deps
COPY . /code/