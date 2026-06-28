import os
import time
import requests


class TelegramSender:

    def __init__(self):

        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")

    def send(self, message):

        if not self.token or not self.chat_id:
            print("Telegram configuration not found.")
            return

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True,
        }

        try:

            response = requests.post(
                url,
                json=payload,
                timeout=30,
            )

            if response.status_code == 200:
                print("Telegram Send Complete")

            else:
                print(response.text)

        except Exception as e:
            print(e)

    def send_markdown_file(self, file_path):

        if not self.token or not self.chat_id:
            print("Telegram configuration not found.")
            return

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore",
        ) as f:

            text = f.read()

        chunks = [
            text[i:i + 3900]
            for i in range(0, len(text), 3900)
        ]

        print(f"Sending {len(chunks)} Telegram message(s)...")

        for index, chunk in enumerate(chunks, start=1):

            self.send(chunk)

            if index != len(chunks):
                time.sleep(1)

        print("Telegram Markdown File Complete")