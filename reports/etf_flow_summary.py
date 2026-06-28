from features.etf_flow_engine import ETFFlowEngine


engine = ETFFlowEngine()
df = engine.run(None)

if df.empty:
    print("ETF Flow 데이터가 없습니다.")
    quit()

print("=" * 80)
print("ALPHA HUNTER ETF FLOW SUMMARY")
print("=" * 80)
print(df.to_string(index=False))
print("=" * 80)

top = df.iloc[0]
bottom = df.iloc[-1]

print("Strongest ETF:", top["ETF"], round(top["FLOW_SCORE"], 2), top["FLOW_STATE"])
print("Weakest ETF:", bottom["ETF"], round(bottom["FLOW_SCORE"], 2), bottom["FLOW_STATE"])
print("=" * 80)