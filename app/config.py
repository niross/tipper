import os

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///")
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
