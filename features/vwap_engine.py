import pandas as pd


def add_vwap(df: pd.DataFrame) -> pd.DataFrame:
    typical_price = (df["high"] + df["low"] + df["close"]) / 3

    volume = df["tick_volume"].replace(0, 1)

    df["VWAP"] = (
        (typical_price * volume).cumsum()
        / volume.cumsum()
    )

    df["VWAP_DISTANCE"] = df["close"] - df["VWAP"]

    df["VWAP_DISTANCE_PCT"] = (
        df["VWAP_DISTANCE"] / df["VWAP"]
    ) * 100

    df["VWAP_ANGLE"] = df["VWAP"].diff()

    df["VWAP_ABOVE"] = df["close"] > df["VWAP"]

    return df