from pathlib import Path
from datetime import datetime

from ai.ai_context_builder import AIContextBuilder
from ai.final_decision_engine import FinalDecisionEngine
from notifications.telegram_sender import TelegramSender
from reports.obsidian_export_v2 import export_report


def main():

    print("=" * 80)
    print("ALPHA HUNTER v3 INSTITUTIONAL PIPELINE")
    print("=" * 80)

    context = AIContextBuilder().build()

    result = FinalDecisionEngine().run(
        context,
    )

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    reports_dir = Path("research") / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    report_file = reports_dir / f"alpha_report_{timestamp}.md"

    report = f"""# Alpha Hunter Institutional Report

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

    export_report(report_file)

    print()
    print("=" * 80)
    print("ALPHA HUNTER COMPLETE")
    print("=" * 80)
    print(f"Report    : {report_file}")
    print("Telegram  : Complete")
    print("Obsidian  : Export Complete")
    print("=" * 80)


if __name__ == "__main__":
    main()