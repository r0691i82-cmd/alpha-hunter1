from pathlib import Path
from datetime import datetime
import shutil

from ai.final_decision_engine import FinalDecisionEngine
from notifications.telegram_sender import TelegramSender


def main():

    print("=" * 80)
    print("ALPHA HUNTER v3 INSTITUTIONAL PIPELINE")
    print("=" * 80)

    result = FinalDecisionEngine().run()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / f"alpha_report_{timestamp}.md"

    report = f"""
# Alpha Hunter Institutional Report

Generated : {datetime.now()}

---

# Analyst

{result["analyst"]}

---

# Bear

{result["bear"]}

---

# Bull

{result["bull"]}

---

# Risk Manager

{result["risk"]}

---

# Final Judge

{result["judge"]}
"""

    report_file.write_text(
        report,
        encoding="utf-8",
    )

    print()
    print("Report Saved")
    print(report_file)

    TelegramSender().send_markdown_file(
        report_file,
    )

    vault = Path("research") / "obsidian_daily"

    vault.mkdir(
        parents=True,
        exist_ok=True,
    )

    destination = vault / report_file.name

    shutil.copy(
        report_file,
        destination,
    )

    print()
    print("=" * 80)
    print("ALPHA HUNTER COMPLETE")
    print("=" * 80)
    print(f"Report    : {report_file}")
    print(f"Obsidian  : {destination}")
    print("Telegram  : Complete")
    print("=" * 80)


if __name__ == "__main__":
    main()