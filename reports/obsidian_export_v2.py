import sys
import shutil
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))


def main():
    report_files = sorted(Path("reports").glob("global_intelligence_report_*.md"))

    if not report_files:
        print("복사할 Global Intelligence Report가 없습니다.")
        return

    latest_report = report_files[-1]

    today = datetime.now().strftime("%Y-%m-%d")
    target_dir = Path("research") / "obsidian_daily"
    target_dir.mkdir(parents=True, exist_ok=True)

    target_file = target_dir / f"{today}_Alpha_Hunter_Global_Intelligence.md"

    shutil.copy(latest_report, target_file)

    print(f"Obsidian Export Complete: {target_file}")


if __name__ == "__main__":
    main()