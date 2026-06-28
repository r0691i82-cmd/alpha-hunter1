from features.cot_engine import COTEngine


engine = COTEngine()
df = engine.run(None)

if df.empty:
    print("COT 데이터가 없습니다.")
    quit()

print("=" * 100)
print("ALPHA HUNTER COT SUMMARY")
print("=" * 100)

cols = [
    "ASSET",
    "MARKET",
    "DATE",
    "NONCOMM_NET",
    "NET_CHANGE_4W",
    "NET_CHANGE_12W",
    "COT_BIAS",
    "COT_MOMENTUM",
]

available_cols = [c for c in cols if c in df.columns]

print(df[available_cols].to_string(index=False))
print("=" * 100)