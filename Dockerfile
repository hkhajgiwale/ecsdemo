FROM python:3.7.1-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    curl

CMD ["python", "./webserver.py"]