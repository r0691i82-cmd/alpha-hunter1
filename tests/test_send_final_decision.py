from pathlib import Path
import subprocess
import sys


def test_send_final_decision_runs():
    report = Path("reports/final_decision_report_test.md")
    report.write_text(
        "# Test Final Decision Report\n\nTelegram send test.",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "reports.send_final_decision",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Final Decision Report Sent" in result.stdout