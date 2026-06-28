from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).parent

PIPELINE = [
    "reports.global_intelligence_report",
    "reports.analyst_report",
    "reports.bear_report",
    "reports.bull_report",
    "reports.risk_manager_report",
    "reports.judge_report",
    "reports.final_decision_report",
    "reports.send_final_decision",
    "reports.obsidian_export_v2",
]

print("=" * 70)
print("ALPHA HUNTER DAILY PIPELINE START")
print("=" * 70)

for module in PIPELINE:

    print(f"\n>>> Running {module}")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            module,
        ],
        cwd=ROOT,
    )

    if result.returncode != 0:

        print(f"\nFAILED : {module}")

        sys.exit(result.returncode)

print("\n" + "=" * 70)
print("ALPHA HUNTER DAILY PIPELINE END")
print("=" * 70)