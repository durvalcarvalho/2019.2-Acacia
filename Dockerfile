FROM python:3.14.0a3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /code/src