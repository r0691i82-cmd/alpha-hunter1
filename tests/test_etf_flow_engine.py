from features.etf_flow_engine import ETFFlowEngine


def test_etf_flow_engine_runs():
    engine = ETFFlowEngine()
    result = engine.run(None)

    assert result is not None