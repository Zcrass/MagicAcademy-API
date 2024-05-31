FROM python:3.10

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --no-cache-dir -r requirements.txt

