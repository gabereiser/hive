FROM python:3-alpine

RUN mkdir -p /opt/hive/src

WORKDIR /opt/hive

COPY ./requirements.txt /opt/hive/requirements.txt

COPY ./package.json /opt/hive/package.json

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del --no-cache .build-deps

RUN apk add --update nodejs npm node-scss

COPY . /opt/hive

RUN npm install && npx webpack && rm -rf node_modules

EXPOSE 8080

ENTRYPOINT ["./start"]
