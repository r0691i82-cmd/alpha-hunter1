from features.market_regime_engine import MarketRegimeEngine


def test_market_regime_engine_runs():
    engine = MarketRegimeEngine()
    result = engine.run()

    assert result is not None
    assert "MARKET_REGIME" in result
    assert "MONEY_FLOW_SCORE" in result