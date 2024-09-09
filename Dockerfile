FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update \
 && apt-get install -y --no-install-recommends bash git

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

COPY . .