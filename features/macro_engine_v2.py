import pandas as pd
from pathlib import Path

from core.base_engine import BaseEngine


class MacroEngineV2(BaseEngine):
    def __init__(self):
        super().__init__("macro_engine_v2")

    def _find_close_column(self, df: pd.DataFrame):
        for col in df.columns:
            if str(col).strip().lower() == "close":
                return col
        return None

    def _clean_close_series(self, df: pd.DataFrame):
        close_col = self._find_close_column(df)

        if close_col is None:
            return None

        close = pd.to_numeric(df[close_col], errors="coerce")
        close = close.dropna()

        if len(close) < 22:
            return None

        return close

    def process(self, data=None):
        rows = []

        files = list(Path("database/macro").glob("*.csv"))

        for file in files:
            try:
                df = pd.read_csv(file)

                df.columns = [str(c).strip() for c in df.columns]

                close = self._clean_close_series(df)

                if close is None:
                    self.logger.warning(f"Skipped {file.name}: invalid Close data")
                    continue

                rows.append({
                    "asset": file.stem,
                    "last": float(close.iloc[-1]),
                    "ret_5d": float((close.iloc[-1] / close.iloc[-6] - 1) * 100),
                    "ret_20d": float((close.iloc[-1] / close.iloc[-21] - 1) * 100),
                })

            except Exception as e:
                self.logger.exception(f"Failed to process {file.name}: {e}")
                continue

        result = pd.DataFrame(rows)

        if result.empty:
            return result

        result["risk_on_score"] = 0.0

        risk_assets = ["NASDAQ", "SP500", "BTC", "SPY", "QQQ", "IWM"]
        risk_off_assets = ["VIX", "DXY", "UUP"]
        defensive_assets = ["GOLD", "TLT", "GLD"]

        result.loc[
            result["asset"].isin(risk_assets),
            "risk_on_score",
        ] = result["ret_20d"]

        result.loc[
            result["asset"].isin(risk_off_assets),
            "risk_on_score",
        ] = -result["ret_20d"]

        result.loc[
            result["asset"].isin(defensive_assets),
            "risk_on_score",
        ] = -result["ret_20d"] * 0.5

        macro_score = float(result["risk_on_score"].mean())

        if macro_score > 1:
            macro_state = "RISK_ON"
        elif macro_score < -1:
            macro_state = "RISK_OFF"
        else:
            macro_state = "NEUTRAL"

        result["MACRO_SCORE"] = macro_score
        result["MACRO_STATE"] = macro_state

        return result