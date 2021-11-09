FROM python:3.9-alpine

# Envs
ENV DJANGOAPP=/usr/src/back
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LIBRARY_PATH=/lib:/usr/lib

# Install psycopg2 and pillow dependencies
RUN apk update \
    && apk add gcc python3-dev musl-dev py3-setuptools jpeg-dev zlib-dev libffi-dev musl-dev openssl-dev cargo

WORKDIR $DJANGOAPP/

RUN pip install --upgrade pip
COPY ./requirements.txt $DJANGOAPP/requirements.txt
RUN pip install -r requirements.txt

COPY . $DJANGOAPP
EXPOSE 8000