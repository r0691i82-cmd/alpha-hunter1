import pandas as pd
from pathlib import Path


def load_last_return(name):
    file = Path(f"database/macro/{name}.csv")

    if not file.exists():
        return None

    df = pd.read_csv(file)

    if len(df) < 22:
        return None

    close = df["Close"]

    return {
        "last": close.iloc[-1],
        "ret_5d": (close.iloc[-1] / close.iloc[-6] - 1) * 100,
        "ret_20d": (close.iloc[-1] / close.iloc[-21] - 1) * 100,
    }


def build_macro_score():
    assets = [
        "DXY",
        "USDJPY",
        "GOLD",
        "SILVER",
        "WTI",
        "VIX",
        "NASDAQ",
        "SP500",
        "BTC",
        "SPY",
        "QQQ",
        "IWM",
        "TLT",
        "GLD",
        "SLV",
        "USO",
        "UUP",
    ]

    rows = []

    for asset in assets:
        data = load_last_return(asset)

        if data is None:
            continue

        rows.append({
            "asset": asset,
            "last": data["last"],
            "ret_5d": data["ret_5d"],
            "ret_20d": data["ret_20d"],
        })

    df = pd.DataFrame(rows)

    if df.empty:
        return df

    df["risk_on_score"] = 0

    df.loc[df["asset"].isin(["NASDAQ", "SP500", "BTC", "SPY", "QQQ", "IWM"]), "risk_on_score"] = df["ret_20d"]
    df.loc[df["asset"].isin(["VIX", "DXY", "UUP"]), "risk_on_score"] = -df["ret_20d"]
    df.loc[df["asset"].isin(["GOLD", "TLT", "GLD"]), "risk_on_score"] = -df["ret_20d"] * 0.5

    macro_score = df["risk_on_score"].mean()

    if macro_score > 1:
        macro_state = "RISK_ON"
    elif macro_score < -1:
        macro_state = "RISK_OFF"
    else:
        macro_state = "NEUTRAL"

    df["MACRO_SCORE"] = macro_score
    df["MACRO_STATE"] = macro_state

    return df