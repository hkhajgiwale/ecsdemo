FROM python:3.7.1

WORKDIR /usr/src/app

COPY . .

CMD ["python", "./webserver.py"]