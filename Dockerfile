FROM python:3-alpine

RUN mkdir -p /opt/hive/src

WORKDIR /opt/hive

# Copy over requirements and install them so it's cached and speeds up build time.
COPY ./requirements.txt /opt/hive/requirements.txt

RUN apk add --update \
    gcc \
    build-base \
    python3-dev \
    musl-dev \
    libpq \
    postgresql-dev \
    && pip install --upgrade pip \
    && pip install psycopg2 \
    && pip install --no-cache-dir -r requirements.txt

COPY . /opt/hive

EXPOSE 8080

ENTRYPOINT ["./scripts/start"]
