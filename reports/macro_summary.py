from features.macro_engine import build_macro_score


df = build_macro_score()

if df.empty:
    print("Macro 데이터가 없습니다.")
    quit()

last_macro_score = df["MACRO_SCORE"].iloc[-1]
last_macro_state = df["MACRO_STATE"].iloc[-1]

print("=" * 80)
print("ALPHA HUNTER MACRO SUMMARY")
print("=" * 80)
print("Macro Score:", round(last_macro_score, 2))
print("Macro State:", last_macro_state)
print("=" * 80)

print(df[["asset", "last", "ret_5d", "ret_20d", "risk_on_score"]].to_string(index=False))

print("=" * 80)