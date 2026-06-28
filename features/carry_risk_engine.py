import pandas as pd
from pathlib import Path


def load_macro(asset):
    file = Path(f"database/macro/{asset}.csv")

    if not file.exists():
        return None

    df = pd.read_csv(file)

    if len(df) < 22:
        return None

    return df


def build_carry_risk_score():
    usdjpy = load_macro("USDJPY")
    vix = load_macro("VIX")
    dxy = load_macro("DXY")
    tlt = load_macro("TLT")

    if usdjpy is None or vix is None or dxy is None or tlt is None:
        return {
            "CARRY_RISK_SCORE": 50,
            "CARRY_RISK_STATE": "UNKNOWN",
        }

    usdjpy_ret = (usdjpy["Close"].iloc[-1] / usdjpy["Close"].iloc[-21] - 1) * 100
    vix_ret = (vix["Close"].iloc[-1] / vix["Close"].iloc[-6] - 1) * 100
    dxy_ret = (dxy["Close"].iloc[-1] / dxy["Close"].iloc[-21] - 1) * 100
    tlt_ret = (tlt["Close"].iloc[-1] / tlt["Close"].iloc[-21] - 1) * 100

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