FROM python:3-alpine

RUN mkdir -p /opt/hive/src

WORKDIR /opt/hive

COPY ./requirements.txt /opt/hive/requirements.txt

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del --no-cache .build-deps

COPY . /opt/hive

EXPOSE 8080

ENTRYPOINT ["./start"]
