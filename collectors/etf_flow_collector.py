import yfinance as yf
from pathlib import Path

from core.base_collector import BaseCollector


ETF_TICKERS = {
    "SPY": "SPY",
    "QQQ": "QQQ",
    "IWM": "IWM",
    "TLT": "TLT",
    "GLD": "GLD",
    "SLV": "SLV",
    "USO": "USO",
    "UUP": "UUP",
}


class ETFFlowCollector(BaseCollector):
    def __init__(self):
        super().__init__("etf_flow_collector")

    def collect(self):
        Path("database/etf").mkdir(parents=True, exist_ok=True)

        for name, ticker in ETF_TICKERS.items():
            self.logger.info(f"Collecting ETF {name} -> {ticker}")

            df = yf.download(
                ticker,
                period="6mo",
                interval="1d",
                progress=False,
                auto_adjust=False,
            )

            if df.empty:
                self.logger.warning(f"No ETF data: {name}")
                continue

            file_path = f"database/etf/{name}.csv"
            df.reset_index().to_csv(file_path, index=False)

            self.logger.info(f"Saved {file_path}")

        return True


if __name__ == "__main__":
    collector = ETFFlowCollector()
    collector.run()