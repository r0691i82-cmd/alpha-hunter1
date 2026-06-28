from ai.ai_context_builder import AIContextBuilder


def test_ai_context_builder_runs():
    context = AIContextBuilder().build()

    assert context is not None
    assert "money_flow" in context
    assert "market_regime" in context
    assert "etf_flow" in context
    assert "cot_positioning" in context
    assert "macro_snapshot" in context