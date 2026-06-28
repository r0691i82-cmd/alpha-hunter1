from features.money_flow_engine import MoneyFlowEngine


def test_money_flow_engine_runs():
    engine = MoneyFlowEngine()
    result = engine.run()

    assert result is not None
    assert "MONEY_FLOW_SCORE" in result
    assert "MARKET_REGIME" in result