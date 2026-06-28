from features.market_regime_engine import MarketRegimeEngine


engine = MarketRegimeEngine()
result = engine.run()

print("=" * 80)
print("ALPHA HUNTER MARKET REGIME SUMMARY")
print("=" * 80)

for key, value in result.items():
    print(f"{key}: {value}")

print("=" * 80)