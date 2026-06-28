import pandas as pd


FILE = "database/BTC_BTCUSD_M5.csv"

df = pd.read_csv(FILE)
last = df.iloc[-1]

print("=" * 60)
print("ALPHA HUNTER DAILY SUMMARY")
print("=" * 60)
print("Asset:", "BTC")
print("Close:", round(last["close"], 4))
print("-" * 60)
print("Alpha Score:", round(last["ALPHA_SCORE"], 2))
print("Structure Score:", round(last["STRUCTURE_SCORE"], 2))
print("Structure State:", last["STRUCTURE_STATE"])
print("Fear Score:", round(last["FEAR_SCORE"], 2))
print("Pattern Score:", round(last["PATTERN_SCORE"], 2))
print("Trend Engine Score:", round(last["TREND_ENGINE_SCORE"], 2))
print("Smart Money Score:", round(last["SMART_MONEY_SCORE"], 2))
print("MTF Score:", round(last["MTF_SCORE"], 2))
print("AI Base Score:", round(last["AI_BASE_SCORE"], 2))
print("-" * 60)
print("AI Signal:", last["AI_SIGNAL"])
print("Final Decision:", last["FINAL_DECISION"])
print("Position Size:", last["POSITION_SIZE_LEVEL"])
print("Risk Level:", last["RISK_LEVEL"])
print("Stop Loss:", round(last["STOP_LOSS"], 4))
print("Take Profit:", round(last["TAKE_PROFIT"], 4))
print("-" * 60)
print("Quarter Zone:", last["DAY_QUARTER_ZONE"])
print("VWAP Distance %:", round(last["VWAP_DISTANCE_PCT"], 4))
print("=" * 60)