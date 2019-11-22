FROM python:3.6-alpine

RUN apk --no-cache update \
 && apk upgrade \
 # development only!
 && apk add --no-cache tree nano git 

COPY src ./app

WORKDIR /app

RUN pip3 install -r docs/requirements.txt


