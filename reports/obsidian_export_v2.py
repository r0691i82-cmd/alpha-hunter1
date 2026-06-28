import sys
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))


def export_report(report_file):
    target_dir = Path("research") / "obsidian_daily"

    target_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    destination = target_dir / Path(report_file).name

    shutil.copy(
        report_file,
        destination,
    )

    print(f"Obsidian Export Complete : {destination}")

    return destination


def main():
    reports = sorted(
        (Path("research") / "reports").glob("alpha_report_*.md")
    )

    if not reports:
        print("복사할 Alpha Report가 없습니다.")
        return

    latest_report = reports[-1]

    export_report(latest_report)


if __name__ == "__main__":
    main()