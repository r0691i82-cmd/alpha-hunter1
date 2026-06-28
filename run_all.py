from collectors.macro_collector_v2 import MacroCollectorV2
from collectors.etf_flow_collector import ETFFlowCollector
from collectors.cot_collector import COTCollector

from features.money_flow_engine import MoneyFlowEngine
from features.market_regime_engine import MarketRegimeEngine

from ai.ai_context_builder import AIContextBuilder
from ai.report_generator import AIReportGenerator

from pathlib import Path
from datetime import datetime


def main():
    print("=" * 80)
    print("ALPHA HUNTER DAILY PIPELINE START")
    print("=" * 80)

    MacroCollectorV2().run()
    ETFFlowCollector().run()
    COTCollector().run()

    money_flow = MoneyFlowEngine().run()
    regime = MarketRegimeEngine().run()
    context = AIContextBuilder().build()
    report = AIReportGenerator().generate_offline_report()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    output_file = Path("reports") / f"daily_pipeline_report_{timestamp}.md"
    output_file.write_text(report, encoding="utf-8")

    print("Money Flow:", money_flow)
    print("Market Regime:", regime)
    print("AI Context Keys:", list(context.keys()))
    print(f"Daily Pipeline Report Saved: {output_file}")

    print("=" * 80)
    print("ALPHA HUNTER DAILY PIPELINE END")
    print("=" * 80)


if __name__ == "__main__":
    main()