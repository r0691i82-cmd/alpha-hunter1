import pandas as pd


def add_smart_money_features(df: pd.DataFrame) -> pd.DataFrame:
    df["SWING_HIGH"] = (
        (df["high"] > df["high"].shift(1))
        & (df["high"] > df["high"].shift(2))
        & (df["high"] > df["high"].shift(-1))
        & (df["high"] > df["high"].shift(-2))
    )

    df["SWING_LOW"] = (
        (df["low"] < df["low"].shift(1))
        & (df["low"] < df["low"].shift(2))
        & (df["low"] < df["low"].shift(-1))
        & (df["low"] < df["low"].shift(-2))
    )

    df["LAST_SWING_HIGH"] = df["high"].where(df["SWING_HIGH"]).ffill()
    df["LAST_SWING_LOW"] = df["low"].where(df["SWING_LOW"]).ffill()

    df["BOS_BULL"] = df["close"] > df["LAST_SWING_HIGH"].shift(1)
    df["BOS_BEAR"] = df["close"] < df["LAST_SWING_LOW"].shift(1)

    df["CHOCH_BULL"] = (
        df["BOS_BULL"]
        & (df["close"].shift(1) < df["EMA_32"].shift(1))
    )

    df["CHOCH_BEAR"] = (
        df["BOS_BEAR"]
        & (df["close"].shift(1) > df["EMA_32"].shift(1))
    )

    df["FVG_BULL"] = df["low"] > df["high"].shift(2)
    df["FVG_BEAR"] = df["high"] < df["low"].shift(2)

    df["LIQUIDITY_GRAB_HIGH"] = (
        (df["high"] > df["LAST_SWING_HIGH"].shift(1))
        & (df["close"] < df["LAST_SWING_HIGH"].shift(1))
    )

    df["LIQUIDITY_GRAB_LOW"] = (
        (df["low"] < df["LAST_SWING_LOW"].shift(1))
        & (df["close"] > df["LAST_SWING_LOW"].shift(1))
    )

    df["SMART_MONEY_SCORE"] = 0

    df.loc[df["BOS_BULL"], "SMART_MONEY_SCORE"] += 25
    df.loc[df["CHOCH_BULL"], "SMART_MONEY_SCORE"] += 25
    df.loc[df["FVG_BULL"], "SMART_MONEY_SCORE"] += 15
    df.loc[df["LIQUIDITY_GRAB_LOW"], "SMART_MONEY_SCORE"] += 25

    df.loc[df["BOS_BEAR"], "SMART_MONEY_SCORE"] -= 25
    df.loc[df["CHOCH_BEAR"], "SMART_MONEY_SCORE"] -= 25
    df.loc[df["FVG_BEAR"], "SMART_MONEY_SCORE"] -= 15
    df.loc[df["LIQUIDITY_GRAB_HIGH"], "SMART_MONEY_SCORE"] -= 25

    return df