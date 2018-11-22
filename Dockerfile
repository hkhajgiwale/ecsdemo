FROM python:3.7.1-alpine

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

RUN apk add --update \
    curl \
  && rm -rf /var/cache/apk/*

CMD ["python", "./webserver.py"]