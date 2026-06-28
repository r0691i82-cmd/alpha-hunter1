import pandas as pd


def add_relative_strength(df: pd.DataFrame) -> pd.DataFrame:
    df["RETURN_1"] = df["close"].pct_change(1)
    df["RETURN_5"] = df["close"].pct_change(5)
    df["RETURN_20"] = df["close"].pct_change(20)

    df["RS_SCORE"] = (
        df["RETURN_1"].fillna(0) * 0.2
        + df["RETURN_5"].fillna(0) * 0.3
        + df["RETURN_20"].fillna(0) * 0.5
    ) * 100

    return df