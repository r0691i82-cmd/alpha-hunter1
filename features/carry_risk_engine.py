import pandas as pd
from pathlib import Path


def load_macro(asset):
    file = Path(f"database/macro/{asset}.csv")

    if not file.exists():
        return None

    df = pd.read_csv(file)
    df.columns = [str(c).strip() for c in df.columns]

    if len(df) < 22:
        return None

    return df


def clean_close(df):
    if df is None:
        return None

    if "Close" not in df.columns:
        return None

    df = df.copy()
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df = df.dropna(subset=["Close"])

    if len(df) < 22:
        return None

    return df


def calc_return(df, days):
    if df is None:
        return 0

    if len(df) <= days:
        return 0

    latest = df["Close"].iloc[-1]
    previous = df["Close"].iloc[-days - 1]

    if previous == 0:
        return 0

    return (latest / previous - 1) * 100


def build_carry_risk_score():
    usdjpy = clean_close(load_macro("USDJPY"))
    vix = clean_close(load_macro("VIX"))
    dxy = clean_close(load_macro("DXY"))
    tlt = clean_close(load_macro("TLT"))

    if usdjpy is None or vix is None or dxy is None or tlt is None:
        return {
            "CARRY_RISK_SCORE": 50,
            "CARRY_RISK_STATE": "UNKNOWN",
        }

    usdjpy_ret = calc_return(usdjpy, 20)
    vix_ret = calc_return(vix, 5)
    dxy_ret = calc_return(dxy, 20)
    tlt_ret = calc_return(tlt, 20)

    score = 50

    if usdjpy_ret < -2:
        score += 25

    if vix_ret > 10:
        score += 25

    if dxy_ret < -1:
        score += 10

    if tlt_ret > 3:
        score += 15

    score = max(0, min(100, score))

    if score >= 75:
        state = "HIGH"
    elif score >= 55:
        state = "MEDIUM"
    else:
        state = "LOW"

    return {
        "CARRY_RISK_SCORE": score,
        "CARRY_RISK_STATE": state,
        "USDJPY_20D_RETURN": usdjpy_ret,
        "VIX_5D_RETURN": vix_ret,
        "DXY_20D_RETURN": dxy_ret,
        "TLT_20D_RETURN": tlt_ret,
    }