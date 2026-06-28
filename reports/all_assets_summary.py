import pandas as pd
from pathlib import Path


FILES = list(Path("database").glob("*_M5.csv"))

print("=" * 90)
print("ALPHA HUNTER ALL ASSETS SUMMARY")
print("=" * 90)

for file in FILES:
    df = pd.read_csv(file)
    last = df.iloc[-1]

    print()
    print("FILE:", file.name)
    print("-" * 90)
    print("Close:", round(last["close"], 4))
    print("AI Signal:", last["AI_SIGNAL"])
    print("Final Decision:", last["FINAL_DECISION"])
    print("Risk Level:", last["RISK_LEVEL"])
    print("AI Base Score:", round(last["AI_BASE_SCORE"], 2))
    print("Structure:", last["STRUCTURE_STATE"])
    print("Quarter:", last["DAY_QUARTER_ZONE"])
    print("Stop Loss:", round(last["STOP_LOSS"], 4))
    print("Take Profit:", round(last["TAKE_PROFIT"], 4))

print()
print("=" * 90)
print("END")
print("=" * 90)