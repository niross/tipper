FROM python:3.9 AS base
WORKDIR /tipper

FROM base AS dev
COPY requirements-dev.txt /tipper/requirements-dev.txt
COPY ./alembic.ini /tipper/alembic.ini
COPY ./compose/start-dev.sh /tipper/start-dev.sh
RUN pip install --no-cache-dir -r /tipper/requirements-dev.txt
CMD ["/tipper/start-dev.sh"]

FROM base as staging
COPY requirements.txt /tipper/requirements.txt
COPY alembic.ini /tipper/alembic.ini
COPY alembic /tipper/alembic
COPY ./compose/start-staging.sh /tipper/start-staging.sh
COPY ./compose/traefik/certinfo.staging.yml /tipper/certinfo.yml
COPY ./app /tipper/app
RUN pip install --no-cache-dir -r /tipper/requirements.txt
CMD ["/tipper/start-staging.sh"]

FROM staging as prod
COPY ./compose/start.sh /tipper/start.sh
CMD ["/tipper/start.sh"]
