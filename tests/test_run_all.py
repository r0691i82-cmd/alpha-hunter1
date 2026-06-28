import subprocess
import sys
from pathlib import Path


def test_run_all_pipeline():
    result = subprocess.run(
        [sys.executable, "run_all.py"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "ALPHA HUNTER DAILY PIPELINE END" in result.stdout

    files = list(Path("reports").glob("daily_pipeline_report_*.md"))
    assert len(files) > 0