from features.money_flow_engine import MoneyFlowEngine


engine = MoneyFlowEngine()
result = engine.run()

print("=" * 80)
print("ALPHA HUNTER GLOBAL MONEY FLOW SUMMARY")
print("=" * 80)

for key, value in result.items():
    print(f"{key}: {value}")

print("=" * 80)