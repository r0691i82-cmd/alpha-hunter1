from features.carry_risk_engine import build_carry_risk_score


result = build_carry_risk_score()

print("=" * 80)
print("ALPHA HUNTER CARRY RISK SUMMARY")
print("=" * 80)

for key, value in result.items():
    if isinstance(value, float):
        print(key, ":", round(value, 2))
    else:
        print(key, ":", value)

print("=" * 80)