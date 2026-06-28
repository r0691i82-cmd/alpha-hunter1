import yfinance as yf
from pathlib import Path

from core.base_collector import BaseCollector


MACRO_TICKERS = {
    "DXY": "DX-Y.NYB",
    "USDJPY": "USDJPY=X",
    "GOLD": "GC=F",
    "SILVER": "SI=F",
    "WTI": "CL=F",
    "VIX": "^VIX",
    "NASDAQ": "^IXIC",
    "SP500": "^GSPC",
    "BTC": "BTC-USD",
    "SPY": "SPY",
    "QQQ": "QQQ",
    "IWM": "IWM",
    "TLT": "TLT",
    "GLD": "GLD",
    "SLV": "SLV",
    "USO": "USO",
    "UUP": "UUP",
}


class MacroCollectorV2(BaseCollector):
    def __init__(self):
        super().__init__("macro_collector_v2")

    def collect(self):
        Path("database/macro").mkdir(parents=True, exist_ok=True)

        for name, ticker in MACRO_TICKERS.items():
            self.logger.info(f"Collecting {name} -> {ticker}")

            df = yf.download(
                ticker,
                period="6mo",
                interval="1d",
                progress=False,
                auto_adjust=False,
            )

            if df.empty:
                self.logger.warning(f"No data: {name}")
                continue

            file_path = f"database/macro/{name}.csv"
            df.reset_index().to_csv(file_path, index=False)

            self.logger.info(f"Saved {file_path}")

        return True


if __name__ == "__main__":
    collector = MacroCollectorV2()
    collector.run()