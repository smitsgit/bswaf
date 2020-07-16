# pull official base image
FROM python:3.8.3-slim-buster

# set working directory
CMD mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
# COPY ./requirements-dev.txt .
RUN pip install -r requirements.txt

# add app
COPY . .
# RUN pip install -e .
# CMD gunicorn -b 0.0.0.0:8000  --access-logfile - "snakeeyes.app:create_app()"
