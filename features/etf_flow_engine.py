import pandas as pd
from pathlib import Path

from core.base_engine import BaseEngine


class ETFFlowEngine(BaseEngine):
    def __init__(self):
        super().__init__("etf_flow_engine")

    def _load_close(self, file: Path):
        df = pd.read_csv(file)
        df.columns = [str(c).strip() for c in df.columns]

        if "Close" not in df.columns:
            return None

        close = pd.to_numeric(df["Close"], errors="coerce").dropna()

        if len(close) < 22:
            return None

        return close

    def process(self, data=None):
        rows = []

        files = list(Path("database/etf").glob("*.csv"))

        for file in files:
            close = self._load_close(file)

            if close is None:
                self.logger.warning(f"Skipped ETF file: {file.name}")
                continue

            rows.append({
                "ETF": file.stem,
                "LAST": float(close.iloc[-1]),
                "RETURN_5D": float((close.iloc[-1] / close.iloc[-6] - 1) * 100),
                "RETURN_20D": float((close.iloc[-1] / close.iloc[-21] - 1) * 100),
            })

        df = pd.DataFrame(rows)

        if df.empty:
            return df

        df["FLOW_SCORE"] = df["RETURN_20D"]

        df["FLOW_STATE"] = "NEUTRAL"
        df.loc[df["FLOW_SCORE"] > 2, "FLOW_STATE"] = "INFLOW"
        df.loc[df["FLOW_SCORE"] < -2, "FLOW_STATE"] = "OUTFLOW"

        return df.sort_values("FLOW_SCORE", ascending=False)