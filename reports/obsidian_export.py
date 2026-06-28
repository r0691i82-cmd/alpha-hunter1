from pathlib import Path
from datetime import datetime
import shutil


REPORTS_DIR = Path("reports")
OBSIDIAN_DIR = Path("research/obsidian_daily")

OBSIDIAN_DIR.mkdir(parents=True, exist_ok=True)

reports = sorted(REPORTS_DIR.glob("alpha_report_*.md"))

if not reports:
    print("복사할 Markdown 리포트가 없습니다.")
    quit()

latest_report = reports[-1]

today = datetime.now().strftime("%Y-%m-%d")
target_file = OBSIDIAN_DIR / f"{today}_Alpha_Hunter_Report.md"

shutil.copy(latest_report, target_file)

print(f"Obsidian Export Complete: {target_file}")