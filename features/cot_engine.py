from pathlib import Path
import pandas as pd

from core.base_engine import BaseEngine


TARGET_MARKETS = {
    "JPY": ["JAPANESE YEN"],
    "GOLD": ["GOLD"],
    "SILVER": ["SILVER"],
    "WTI": ["CRUDE OIL", "LIGHT SWEET CRUDE"],
    "SP500": ["S&P", "E-MINI S&P"],
    "NASDAQ": ["NASDAQ", "NASDAQ-100"],
    "US_BOND": ["TREASURY BONDS", "TREASURY NOTES", "10-YEAR"],
}


class COTEngine(BaseEngine):
    def __init__(self):
        super().__init__("cot_engine")

    def _find_column(self, df: pd.DataFrame, candidates: list[str]):
        normalized = {c.lower(): c for c in df.columns}

        for candidate in candidates:
            key = candidate.lower()
            if key in normalized:
                return normalized[key]

        for col in df.columns:
            low = col.lower()
            for candidate in candidates:
                if candidate.lower() in low:
                    return col

        return None

    def _load_data(self):
        file = Path("database/cot/cot_legacy_futures.csv")

        if not file.exists():
            self.logger.warning("COT file not found")
            return pd.DataFrame()

        df = pd.read_csv(file)
        df.columns = [str(c).strip() for c in df.columns]

        return df

    def _market_filter(self, df: pd.DataFrame, market_col: str, keywords: list[str]):
        mask = pd.Series(False, index=df.index)

        for keyword in keywords:
            mask = mask | df[market_col].astype(str).str.upper().str.contains(
                keyword.upper(),
                na=False,
            )

        return df[mask].copy()

    def process(self, data=None):
        df = self._load_data()

        if df.empty:
            return pd.DataFrame()

        market_col = self._find_column(
            df,
            ["market_and_exchange_names", "market", "market_name"],
        )

        date_col = self._find_column(
            df,
            ["report_date_as_yyyy_mm_dd", "report_date", "date"],
        )

        long_col = self._find_column(
            df,
            ["noncommercial_positions_long_all", "noncomm_positions_long_all"],
        )

        short_col = self._find_column(
            df,
            ["noncommercial_positions_short_all", "noncomm_positions_short_all"],
        )

        open_interest_col = self._find_column(
            df,
            ["open_interest_all", "open_interest"],
        )

        required = [market_col, date_col, long_col, short_col]

        if any(col is None for col in required):
            self.logger.error("Required COT columns missing")
            self.logger.info(f"Available columns: {df.columns.tolist()}")
            return pd.DataFrame()

        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
        df[long_col] = pd.to_numeric(df[long_col], errors="coerce")
        df[short_col] = pd.to_numeric(df[short_col], errors="coerce")

        if open_interest_col:
            df[open_interest_col] = pd.to_numeric(
                df[open_interest_col],
                errors="coerce",
            )

        rows = []

        for asset, keywords in TARGET_MARKETS.items():
            asset_df = self._market_filter(df, market_col, keywords)

            if asset_df.empty:
                self.logger.warning(f"No COT market found for {asset}")
                continue

            asset_df = asset_df.sort_values(date_col)

            latest = asset_df.iloc[-1]
            prev_4w = asset_df.iloc[-5] if len(asset_df) >= 5 else asset_df.iloc[0]
            prev_12w = asset_df.iloc[-13] if len(asset_df) >= 13 else asset_df.iloc[0]

            latest_net = latest[long_col] - latest[short_col]
            net_4w = prev_4w[long_col] - prev_4w[short_col]
            net_12w = prev_12w[long_col] - prev_12w[short_col]

            row = {
                "ASSET": asset,
                "MARKET": latest[market_col],
                "DATE": latest[date_col],
                "NONCOMM_LONG": latest[long_col],
                "NONCOMM_SHORT": latest[short_col],
                "NONCOMM_NET": latest_net,
                "NET_CHANGE_4W": latest_net - net_4w,
                "NET_CHANGE_12W": latest_net - net_12w,
            }

            if open_interest_col:
                row["OPEN_INTEREST"] = latest[open_interest_col]
                if latest[open_interest_col] and latest[open_interest_col] != 0:
                    row["NET_OI_RATIO"] = latest_net / latest[open_interest_col] * 100
                else:
                    row["NET_OI_RATIO"] = 0

            rows.append(row)

        result = pd.DataFrame(rows)

        if result.empty:
            return result

        result["COT_BIAS"] = "NEUTRAL"
        result.loc[result["NONCOMM_NET"] > 0, "COT_BIAS"] = "LONG"
        result.loc[result["NONCOMM_NET"] < 0, "COT_BIAS"] = "SHORT"

        result["COT_MOMENTUM"] = "NEUTRAL"
        result.loc[result["NET_CHANGE_4W"] > 0, "COT_MOMENTUM"] = "IMPROVING"
        result.loc[result["NET_CHANGE_4W"] < 0, "COT_MOMENTUM"] = "DETERIORATING"

        return result