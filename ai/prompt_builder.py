import json

from ai.ai_context_builder import AIContextBuilder


class InstitutionalPromptBuilder:
    def build(self):
        context = AIContextBuilder().build()

        prompt = f"""
You are an institutional macro strategist and professional portfolio manager.

Your job is to analyze the structured market data below.

Rules:
- Do not invent data.
- Do not calculate new indicators.
- Use only the provided structured data.
- Think like an institutional investor.
- Focus on global money flow.
- Identify risk-on / risk-off conditions.
- Explain ETF rotation.
- Explain COT positioning.
- Explain macro regime.
- Provide bullish and bearish scenarios.
- Provide final investment opinion.

Required output:

1. Executive Summary
2. Global Money Flow
3. Market Regime
4. ETF Rotation
5. COT Positioning
6. Macro Risk
7. Bullish Scenario
8. Bearish Scenario
9. Final Decision
10. Risk Warnings

Structured Data:
{json.dumps(context, indent=2, ensure_ascii=False)}
"""
        return prompt.strip()