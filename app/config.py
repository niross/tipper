import os

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///")
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", None)
SENTRY_DSN = os.environ.get("SENTRY_DSN", None)
ATTACHMENTS_DIR = os.environ.get("ATTACHMENTS_DIR", "/tipper/attachments/")
