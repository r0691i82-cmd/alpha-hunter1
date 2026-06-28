import pandas as pd
from pathlib import Path
from datetime import datetime


FILES = list(Path("database").glob("*_M5.csv"))

report_date = datetime.now().strftime("%Y-%m-%d_%H-%M")
output_file = Path("reports") / f"alpha_report_{report_date}.md"

lines = []

lines.append("# Alpha Hunter Market Report")
lines.append("")
lines.append(f"Generated: {datetime.now()}")
lines.append("")

for file in FILES:
    df = pd.read_csv(file)

    if "AI_SIGNAL" not in df.columns:
        print(f"건너뜀: {file.name} → AI_SIGNAL 없음")
        continue

    last = df.iloc[-1]

    lines.append(f"## {file.stem}")
    lines.append("")
    lines.append(f"- Close: {round(last['close'], 4)}")
    lines.append(f"- AI Signal: {last['AI_SIGNAL']}")
    lines.append(f"- Final Decision: {last['FINAL_DECISION']}")
    lines.append(f"- Risk Level: {last['RISK_LEVEL']}")
    lines.append(f"- AI Base Score: {round(last['AI_BASE_SCORE'], 2)}")
    lines.append(f"- Structure State: {last['STRUCTURE_STATE']}")
    lines.append(f"- Quarter Zone: {last['DAY_QUARTER_ZONE']}")
    lines.append(f"- Stop Loss: {round(last['STOP_LOSS'], 4)}")
    lines.append(f"- Take Profit: {round(last['TAKE_PROFIT'], 4)}")
    lines.append("")

output_file.write_text("\n".join(lines), encoding="utf-8")

print(f"Markdown Report Saved: {output_file}")