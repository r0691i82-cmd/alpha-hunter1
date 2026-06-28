import os
import requests


class TelegramSender:

    def __init__(self):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")

    def send(self, message):

        if not self.token:
            print("TELEGRAM_BOT_TOKEN not found")
            return

        if not self.chat_id:
            print("TELEGRAM_CHAT_ID not found")
            return

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }

        r = requests.post(url, json=payload, timeout=30)

        print(r.status_code)