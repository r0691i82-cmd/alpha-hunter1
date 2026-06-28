from ai.final_decision_engine import FinalDecisionEngine

from notifications.telegram_sender import TelegramSender

from pathlib import Path
from datetime import datetime

import shutil


def main():

    print("=" * 80)
    print("ALPHA HUNTER v3")
    print("=" * 80)

    result = FinalDecisionEngine().run()

    report = result["judge"]

    reports = Path("reports")

    reports.mkdir(
        exist_ok=True,
    )

    filename = (
        reports
        /
        f"alpha_report_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"
    )

    filename.write_text(
        report,
        encoding="utf-8",
    )

    TelegramSender().send_markdown_file(
        filename,
    )

    vault = Path(
        "research/obsidian_daily"
    )

    vault.mkdir(
        parents=True,
        exist_ok=True,
    )

    shutil.copy(
        filename,
        vault / filename.name,
    )

    print()
    print("Pipeline Complete")
    print(filename)


if __name__ == "__main__":
    main()