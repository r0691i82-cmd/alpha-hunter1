import json

from ai.base_ai_engine import BaseAIEngine


class JudgeEngine(BaseAIEngine):

    MODEL = "gemini-2.5-pro"

    PROMPT_FILE = "ai/prompts/judge.txt"

    def build_prompt(
        self,
        context,
        analyst_report,
        bear_report,
        bull_report,
        risk_report,
    ):

        context_text = json.dumps(
            context,
            indent=2,
            ensure_ascii=False,
            default=str,
        )

        system_prompt = self.load_prompt()

        return f"""
{system_prompt}

You are the final investment committee judge.

Use only the provided data, internal reports, and institutional memory.

Return:

1. Executive Summary
2. Current Market Regime
3. Global Money Flow
4. Bull Case
5. Bear Case
6. Risk Assessment
7. Scenario 7 Days
8. Scenario 30 Days
9. Best Case
10. Base Case
11. Worst Case
12. Probability Table
13. Portfolio Allocation
14. Trade Plan
15. Confidence Score
16. Final Decision
17. Memory Comparison
18. Regime Change
19. Repeated Mistakes

Structured Data:

{context_text}

Institutional Memory:

{context.get("market_memory", [])}

Analyst Report:

{analyst_report}

Bear Report:

{bear_report}

Bull Report:

{bull_report}

Risk Manager Report:

{risk_report}

Build three independent scenarios.

Scenario A: Bull
Scenario B: Neutral
Scenario C: Bear

For each scenario estimate:

- Probability
- Catalyst
- Target
- Risk
- Invalidation
- Expected ETF Rotation
- Expected COT Change
- Expected Dollar
- Expected Bond Yield
- Expected Gold
- Expected Bitcoin
- Expected Nasdaq

Create a probability table.

The sum must equal 100%.

- Bull %
- Neutral %
- Bear %

Recommend portfolio allocation.

- Cash
- US Equity
- Gold
- Bond
- Bitcoin
- Commodity
- JPY
- USD

Trade Plan:

- Entry
- Stop
- Target
- Risk Reward
- Maximum Position Size
- Maximum Portfolio Risk

Confidence Score Rules:

Below 40: Very Uncertain
40~60: Neutral
60~80: High Confidence
Above 80: Exceptional Conviction

Explain WHY.

Find contradictions between:

- ETF Flow
- Money Flow
- Macro
- Technical
- COT
- Liquidity

If contradictions exist:

- Reduce confidence
- Explain the contradiction
- Explain what data would resolve it

Compare today's market with previous reports.

Find:

- Recurring mistakes
- Regime changes
- Probability changes
- Whether today's conclusion is stronger or weaker than the past week
- Whether current risks are increasing or decreasing
- Whether confidence should be raised or lowered

Avoid repeating previous mistakes.
"""