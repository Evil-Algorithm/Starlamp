# syntax=docker/dockerfile:1
FROM python:3.11-alpine3.17
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app/
COPY requirements.txt /app/

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# update pip
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app/