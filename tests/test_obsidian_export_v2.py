from pathlib import Path
import subprocess
import sys


def test_obsidian_export_v2_runs():
    subprocess.run(
        [
            sys.executable,
            "-m",
            "reports.global_intelligence_report",
        ],
        capture_output=True,
        text=True,
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "reports.obsidian_export_v2",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Obsidian Export Complete" in result.stdout

    files = list(
        Path("research/obsidian_daily").glob(
            "*_Alpha_Hunter_Global_Intelligence.md"
        )
    )
    assert len(files) > 0