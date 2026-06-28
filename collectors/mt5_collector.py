import MetaTrader5 as mt5
import pandas as pd
from pathlib import Path

from core.settings import WATCHLIST
from core.symbol_mapper import resolve_symbol
from features.ema_engine import add_ema
from features.ema_geometry import add_ema_geometry
from features.vwap_engine import add_vwap
from features.momentum_engine import add_momentum_features
from features.relative_strength import add_relative_strength
from features.score_engine import add_score_engine
from features.quarter_zone import add_quarter_zone
from features.liquidity_engine import add_liquidity_features
from features.market_structure import add_market_structure
from features.fear_engine import add_fear_features
from features.pattern_engine import add_pattern_features
from features.trend_engine import add_trend_features
from features.smart_money_engine import add_smart_money_features
from features.multi_timeframe import add_multi_timeframe_features
from features.ai_feature_engine import add_ai_features
from features.decision_engine import add_decision_features

TIMEFRAME = mt5.TIMEFRAME_M5
TIMEFRAME_NAME = "M5"
BARS = 500


def main():
    if not mt5.initialize():
        print("MT5 연결 실패")
        print(mt5.last_error())
        return

    Path("database").mkdir(exist_ok=True)

    for asset in WATCHLIST:
        symbol = resolve_symbol(asset)

        if symbol is None:
            print(f"{asset} → 찾을 수 없음")
            continue

        print(f"{asset} → {symbol}")

        if not mt5.symbol_select(symbol, True):
            print(f"{symbol} 선택 실패")
            continue

        rates = mt5.copy_rates_from_pos(symbol, TIMEFRAME, 0, BARS)

        if rates is None:
            print(f"{symbol} 데이터 실패")
            continue

        df = pd.DataFrame(rates)
        df["time"] = pd.to_datetime(df["time"], unit="s")

        df = add_ema(df)
        df = add_ema_geometry(df)
        df = add_vwap(df)
        df = add_momentum_features(df)
        df = add_relative_strength(df)
        df = add_score_engine(df)
        df = add_quarter_zone(df)
        df = add_liquidity_features(df)
        df = add_market_structure(df)
        df = add_fear_features(df)
        df = add_pattern_features(df)
        df = add_trend_features(df)
        df = add_smart_money_features(df)
        df = add_multi_timeframe_features(df)
        df = add_ai_features(df)
        df = add_decision_features(df)

        filename = f"database/{asset}_{symbol}_{TIMEFRAME_NAME}.csv"
        df.to_csv(filename, index=False)

        print(f"저장 완료: {filename}")

    mt5.shutdown()
    print("전체 완료")


if __name__ == "__main__":
    main()