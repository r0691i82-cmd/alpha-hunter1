import yfinance as yf
import pandas as pd
from pathlib import Path


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


def main():
    Path("database/macro").mkdir(parents=True, exist_ok=True)

    for name, ticker in MACRO_TICKERS.items():
        print(f"수집 중: {name} → {ticker}")

        df = yf.download(
            ticker,
            period="6mo",
            interval="1d",
            progress=False,
            auto_adjust=False,
        )

        if df.empty:
            print(f"실패: {name}")
            continue

        df = df.reset_index()
        df.to_csv(f"database/macro/{name}.csv", index=False)

        print(f"저장 완료: database/macro/{name}.csv")

    print("Macro Collector 완료")


if __name__ == "__main__":
    main()