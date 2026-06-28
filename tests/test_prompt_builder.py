from ai.prompt_builder import InstitutionalPromptBuilder


def test_prompt_builder_runs():
    prompt = InstitutionalPromptBuilder().build()

    assert prompt is not None
    assert "Global Liquidity" in prompt
    assert "ETF Flow" in prompt
    assert "FINAL DECISION FORMAT" in prompt