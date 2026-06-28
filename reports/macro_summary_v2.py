from features.macro_engine_v2 import MacroEngineV2


engine = MacroEngineV2()
df = engine.run(None)

if df.empty:
    print("Macro 데이터가 없습니다.")
    quit()

print("=" * 80)
print("ALPHA HUNTER MACRO SUMMARY V2")
print("=" * 80)
print("Macro Score:", round(df["MACRO_SCORE"].iloc[-1], 2))
print("Macro State:", df["MACRO_STATE"].iloc[-1])
print("=" * 80)
print(df[["asset", "last", "ret_5d", "ret_20d", "risk_on_score"]].to_string(index=False))
print("=" * 80)