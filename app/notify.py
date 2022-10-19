from slack_sdk.webhook import WebhookClient

from app import config


def send_slack_message(message):
    webhook = WebhookClient(config.SLACK_WEBHOOK_URL)
    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"
