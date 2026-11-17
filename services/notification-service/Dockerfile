FROM python:3.13-slim

RUN pip install --upgrade pip
WORKDIR /notification-service

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .