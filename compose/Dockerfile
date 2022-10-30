FROM python:3.9 AS base
WORKDIR /tipper
COPY ./alembic.ini /tipper/alembic.ini

FROM base AS dev
COPY requirements-dev.txt /tipper/requirements-dev.txt
COPY ./compose/start-dev.sh /tipper/start-dev.sh
RUN pip install --no-cache-dir -r /tipper/requirements-dev.txt
CMD ["/tipper/start-dev.sh"]

FROM base as prod_base

FROM prod_base as test
COPY requirements-dev.txt /tipper/requirements-dev.txt
RUN pip install --no-cache-dir -r /tipper/requirements-dev.txt
COPY ./app /tipper/app
RUN mkdir -p /tipper/attachments
COPY ./compose/start-dev.sh /tipper/start-dev.sh
CMD ["/tipper/start-dev.sh"]

FROM prod_base as staging
COPY requirements.txt /tipper/requirements.txt
RUN pip install --no-cache-dir -r /tipper/requirements.txt
COPY ./compose/start-staging.sh /tipper/start-staging.sh
COPY ./compose/traefik/certinfo.staging.yml /tipper/certinfo.yml
COPY ./app /tipper/app
CMD ["/tipper/start-staging.sh"]

FROM prod_base as prod
COPY ./compose/start.sh /tipper/start.sh
CMD ["/tipper/start.sh"]
