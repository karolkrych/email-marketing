FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y gettext libpq-dev python3-dev

RUN mkdir /code
WORKDIR /code
ADD email-marketing /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
