from pathlib import Path
from datetime import datetime

from collectors.macro_collector_v2 import MacroCollectorV2
from collectors.etf_flow_collector import ETFFlowCollector
from collectors.cot_collector import COTCollector

from features.money_flow_engine import MoneyFlowEngine
from features.market_regime_engine import MarketRegimeEngine

from ai.ai_context_builder import AIContextBuilder
from ai.report_generator import AIReportGenerator

from notifications.telegram_sender import TelegramSender


def main():

    print("=" * 80)
    print("ALPHA HUNTER DAILY PIPELINE START")
    print("=" * 80)

    print("[1/7] Macro Collector")
    MacroCollectorV2().run()

    print("[2/7] ETF Collector")
    ETFFlowCollector().run()

    print("[3/7] COT Collector")
    COTCollector().run()

    print("[4/7] Money Flow Engine")
    money_flow = MoneyFlowEngine().run()

    print("[5/7] Market Regime Engine")
    regime = MarketRegimeEngine().run()

    print("[6/7] AI Context Builder")
    context = AIContextBuilder().build()

    print("[7/7] AI Report Generator")
    report = AIReportGenerator().generate_offline_report()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / f"daily_pipeline_report_{timestamp}.md"

    report_file.write_text(
        report,
        encoding="utf-8",
    )

    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)

    print("Money Flow")
    print(money_flow)

    print()

    print("Market Regime")
    print(regime)

    print()

    print("AI Context")
    print(context.keys())

    print()

    print(f"Report Saved : {report_file}")

    try:
        TelegramSender().send(report[:3900])
        print("Telegram Sent")
    except Exception as e:
        print(f"Telegram Error : {e}")

    print()
    print("=" * 80)
    print("ALPHA HUNTER DAILY PIPELINE END")
    print("=" * 80)


if __name__ == "__main__":
    main()