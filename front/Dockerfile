FROM node:14.15.0-alpine

# Envs
ENV REACTAPP=/usr/src/

WORKDIR $REACTAPP/

# Install yarn and dependences
RUN apk update

COPY package.json $REACTAPP/package.json
# COPY package-lock.json $REACTAPP/package-lock.json

RUN npm install

COPY . $REACTAPP
EXPOSE 3000