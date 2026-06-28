import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from features.money_flow_engine import MoneyFlowEngine
from features.market_regime_engine import MarketRegimeEngine
from features.etf_flow_engine import ETFFlowEngine
from features.cot_engine import COTEngine
from features.macro_engine_v2 import MacroEngineV2


def add_section(lines, title):
    lines.append("")
    lines.append(f"## {title}")
    lines.append("")


def main():
    report_time = datetime.now().strftime("%Y-%m-%d_%H-%M")
    output_file = Path("reports") / f"global_intelligence_report_{report_time}.md"

    money_flow = MoneyFlowEngine().run()
    regime = MarketRegimeEngine().run()
    etf = ETFFlowEngine().run(None)
    cot = COTEngine().run(None)
    macro = MacroEngineV2().run(None)

    lines = []

    lines.append("# Alpha Hunter Global Intelligence Report")
    lines.append("")
    lines.append(f"Generated: {datetime.now()}")
    lines.append("")

    add_section(lines, "Global Money Flow")
    lines.append(f"- Money Flow Score: {money_flow.get('MONEY_FLOW_SCORE')}")
    lines.append(f"- Market Regime: {money_flow.get('MARKET_REGIME')}")
    lines.append(f"- Macro State: {money_flow.get('MACRO_STATE')}")

    add_section(lines, "Market Regime")
    lines.append(f"- Regime: {regime.get('MARKET_REGIME')}")
    lines.append(f"- Money Flow Score: {regime.get('MONEY_FLOW_SCORE')}")
    lines.append(f"- Carry Risk Score: {regime.get('CARRY_RISK_SCORE')}")
    lines.append(f"- Carry Risk State: {regime.get('CARRY_RISK_STATE')}")
    lines.append(f"- Macro State: {regime.get('MACRO_STATE')}")

    add_section(lines, "ETF Flow")
    if etf is not None and not etf.empty:
        for _, row in etf.iterrows():
            lines.append(
                f"- {row['ETF']}: {round(row['FLOW_SCORE'], 2)} / {row['FLOW_STATE']}"
            )
    else:
        lines.append("- ETF data unavailable")

    add_section(lines, "COT Positioning")
    if cot is not None and not cot.empty:
        for _, row in cot.iterrows():
            lines.append(
                f"- {row['ASSET']}: {row['COT_BIAS']} / "
                f"{row['COT_MOMENTUM']} / Net {round(row['NONCOMM_NET'], 2)}"
            )
    else:
        lines.append("- COT data unavailable")

    add_section(lines, "Macro Snapshot")
    if macro is not None and not macro.empty:
        for _, row in macro.iterrows():
            lines.append(
                f"- {row['asset']}: 20D {round(row['ret_20d'], 2)} / "
                f"Risk Score {round(row['risk_on_score'], 2)}"
            )
    else:
        lines.append("- Macro data unavailable")

    output_file.write_text("\n".join(lines), encoding="utf-8")

    print(f"Global Intelligence Report Saved: {output_file}")


if __name__ == "__main__":
    main()