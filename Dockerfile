FROM python:3.7.1

RUN pip install requests

WORKDIR /usr/src/app

COPY . .

CMD ["python", "./webserver.py"]