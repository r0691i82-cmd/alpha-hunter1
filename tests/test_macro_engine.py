from features.macro_engine_v2 import MacroEngineV2


def test_macro_engine_runs():
    engine = MacroEngineV2()
    result = engine.run(None)

    assert result is not None