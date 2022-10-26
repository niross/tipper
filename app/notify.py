from slack_sdk.webhook import WebhookClient

from app import config


def send_slack_message(message):
    if config.SLACK_WEBHOOK_URL is None:
        print("Not sending message as slack is not configured", message)
        return
    webhook = WebhookClient(config.SLACK_WEBHOOK_URL)
    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"
