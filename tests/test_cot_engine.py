from features.cot_engine import COTEngine


def test_cot_engine_runs():
    engine = COTEngine()
    result = engine.run(None)

    assert result is not None