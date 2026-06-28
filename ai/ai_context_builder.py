from datetime import datetime
from pathlib import Path

from features.money_flow_engine import MoneyFlowEngine
from features.market_regime_engine import MarketRegimeEngine
from features.etf_flow_engine import ETFFlowEngine
from features.cot_engine import COTEngine
from features.macro_engine_v2 import MacroEngineV2


class AIContextBuilder:

    def build(self):

        money_flow = MoneyFlowEngine().run()
        market_regime = MarketRegimeEngine().run()
        etf_flow = ETFFlowEngine().run(None)
        cot = COTEngine().run(None)
        macro = MacroEngineV2().run(None)

        return {
            "generated_at": datetime.now().isoformat(),
            "money_flow": money_flow,
            "market_regime": market_regime,
            "etf_flow": self._df_to_records(etf_flow),
            "cot_positioning": self._df_to_records(cot),
            "macro_snapshot": self._df_to_records(macro),
            "latest_reports": self._load_latest_reports(),
            "watchlist": [
                "SPY",
                "QQQ",
                "IWM",
                "GLD",
                "SLV",
                "USO",
                "TLT",
                "UUP",
                "BTCUSD",
                "ETHUSD",
                "USDJPY",
                "XAUUSD",
                "USTEC",
            ],
            "decision_rules": {
                "risk_on": "Money flow strong, carry risk low, ETF inflow broadening",
                "risk_off": "Carry risk high, liquidity stress, defensive ETF leadership",
                "neutral": "Mixed signal, wait for confirmation",
            },
        }

    def _df_to_records(self, df):

        if df is None:
            return []

        if hasattr(df, "empty") and df.empty:
            return []

        return df.to_dict(orient="records")

    def _load_latest_reports(self):

        reports_dir = Path("research") / "reports"

        if not reports_dir.exists():
            return []

        reports = sorted(
            reports_dir.glob("alpha_report_*.md")
        )

        items = []

        for report in reports[-3:]:
            items.append({
                "file": str(report),
                "content": report.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )[:3000],
            })

        return items