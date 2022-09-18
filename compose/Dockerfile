FROM python:3.9 AS base
WORKDIR /tipper

FROM base AS dev
COPY requirements-dev.txt /tipper/requirements-dev.txt
COPY ./compose/start-dev.sh /tipper/start-dev.sh
RUN pip install --no-cache-dir -r /tipper/requirements-dev.txt
CMD ["/tipper/start-dev.sh"]

FROM base as prod
COPY requirements.txt /tipper/requirements.txt
COPY ./compose/start.sh /tipper/start.sh
COPY ./app /tipper/app
CMD ["/tipper/start.sh"]
