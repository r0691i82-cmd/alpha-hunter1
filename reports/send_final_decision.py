from pathlib import Path

from notifications.telegram_sender import TelegramSender


files = sorted(Path("reports").glob("final_decision_report_*.md"))

if not files:
    print("No final decision report found.")
    quit()

latest = files[-1]

text = latest.read_text(
    encoding="utf-8",
    errors="ignore",
)

TelegramSender().send(text[:3900])

print("Final Decision Report Sent")