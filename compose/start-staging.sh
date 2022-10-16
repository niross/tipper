#!/usr/bin/env bash

alembic upgrade head
uvicorn app.main:app --host 0.0.0.0 --port 80 --ssl-certfile /certificate/system/default/RSA-fullchain.pem --ssl-keyfile /certificate/system/default/RSA-privkey.pem
