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

You are the Investment Committee Chairman.

This report will be used to allocate institutional capital.

Think like:

Bridgewater
BlackRock
Citadel
Millennium
Point72
Goldman Sachs

====================================================

Institutional Data

{context_text}

====================================================

Institutional Memory

{context.get("market_memory", [])}

====================================================

Analyst

{analyst_report}

====================================================

Bear

{bear_report}

====================================================

Bull

{bull_report}

====================================================

Risk Manager

{risk_report}

====================================================

TASK 1

Evaluate all reports.

Find every contradiction.

====================================================

TASK 2

Score every report.

Analyst Score

Bear Score

Bull Score

Risk Score

====================================================

TASK 3

Market Regime

Risk On

Neutral

Risk Off

Transition

====================================================

TASK 4

Scenario

7 Day

30 Day

90 Day

====================================================

TASK 5

Probability

Bull %

Neutral %

Bear %

Total must equal 100%.

====================================================

TASK 6

Institutional Portfolio

Cash %

US Equity %

Gold %

Bond %

Bitcoin %

Commodity %

JPY %

USD %

====================================================

TASK 7

Trade Plan

Entry

Stop

Target

Risk Reward

Maximum Position Size

Maximum Portfolio Risk

====================================================

TASK 8

Self Reflection

Why might this conclusion be wrong?

What assumptions are weak?

Which data is missing?

Which indicator would completely invalidate today's conclusion?

====================================================

TASK 9

Institutional Alpha Score

Money Flow

ETF Flow

Macro

Liquidity

COT

Technical

Risk

Sentiment

Carry

Volatility

Each Score

0~10

Total

0~100

====================================================

TASK 10

Confidence Calibration

Below 40

Very Low

40~60

Neutral

60~80

High

80~100

Exceptional

Explain WHY.

====================================================

TASK 11

Final Executive Decision

BUY

ACCUMULATE

HOLD

REDUCE

SELL

RISK OFF

====================================================

Return a professional institutional investment report.

Never fabricate data.

Always explain reasoning.

Always compare with previous reports.

Always challenge your own conclusion before giving the final decision.
"""