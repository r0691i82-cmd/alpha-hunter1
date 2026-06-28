import pandas as pd
from pathlib import Path
from datetime import datetime

from features.macro_engine import build_macro_score
from features.carry_risk_engine import build_carry_risk_score


TECH_FILES = list(Path("database").glob("*_M5.csv"))

macro_df = build_macro_score()
carry = build_carry_risk_score()

report_date = datetime.now().strftime("%Y-%m-%d_%H-%M")
output_file = Path("reports") / f"global_daily_report_{report_date}.md"

lines = []

lines.append("# Alpha Hunter Global Daily Report")
lines.append("")
lines.append(f"Generated: {datetime.now()}")
lines.append("")

lines.append("## Macro Summary")
lines.append("")

if not macro_df.empty:
    lines.append(f"- Macro Score: {round(macro_df['MACRO_SCORE'].iloc[-1], 2)}")
    lines.append(f"- Macro State: {macro_df['MACRO_STATE'].iloc[-1]}")
else:
    lines.append("- Macro data unavailable")

lines.append("")

lines.append("## Carry Risk")
lines.append("")
lines.append(f"- Carry Risk Score: {carry.get('CARRY_RISK_SCORE')}")
lines.append(f"- Carry Risk State: {carry.get('CARRY_RISK_STATE')}")
lines.append("")

lines.append("## Technical Assets")
lines.append("")

for file in TECH_FILES:
    df = pd.read_csv(file)

    if "AI_SIGNAL" not in df.columns:
        continue

    last = df.iloc[-1]

    lines.append(f"### {file.stem}")
    lines.append("")
    lines.append(f"- Close: {round(last['close'], 4)}")
    lines.append(f"- AI Signal: {last['AI_SIGNAL']}")
    lines.append(f"- Final Decision: {last['FINAL_DECISION']}")
    lines.append(f"- Risk Level: {last['RISK_LEVEL']}")
    lines.append(f"- AI Base Score: {round(last['AI_BASE_SCORE'], 2)}")
    lines.append(f"- Structure State: {last['STRUCTURE_STATE']}")
    lines.append(f"- Smart Money Score: {round(last['SMART_MONEY_SCORE'], 2)}")
    lines.append(f"- Stop Loss: {round(last['STOP_LOSS'], 4)}")
    lines.append(f"- Take Profit: {round(last['TAKE_PROFIT'], 4)}")
    lines.append("")

output_file.write_text("\n".join(lines), encoding="utf-8")

print(f"Global Daily Report Saved: {output_file}")