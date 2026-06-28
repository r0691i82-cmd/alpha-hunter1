from ai.prompt_builder import InstitutionalPromptBuilder


def test_prompt_builder_runs():
    prompt = InstitutionalPromptBuilder().build()

    assert prompt is not None
    assert "Structured Data" in prompt
    assert "Global Money Flow" in prompt
    assert "Final Decision" in prompt