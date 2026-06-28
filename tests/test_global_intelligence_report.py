from pathlib import Path
import subprocess
import sys


def test_global_intelligence_report_runs():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "reports.global_intelligence_report",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Global Intelligence Report Saved" in result.stdout

    files = list(Path("reports").glob("global_intelligence_report_*.md"))
    assert len(files) > 0