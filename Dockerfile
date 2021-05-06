FROM python:3-alpine

RUN mkdir -p /opt/hive/src

WORKDIR /opt/hive

RUN apk add --update \
    gcc \
    libffi-dev \
    build-base \
    python3-dev \
    musl-dev \
    libpq \
    openssl \
    postgresql-dev

# Copy over requirements and install them so it's cached and speeds up build time.
COPY ./requirements.txt /opt/hive/requirements.txt

RUN pip install --upgrade pip \
    && pip install psycopg2 \
    && pip install --no-cache-dir -r requirements.txt

COPY . /opt/hive

EXPOSE 8080

ENTRYPOINT ["./scripts/start"]
