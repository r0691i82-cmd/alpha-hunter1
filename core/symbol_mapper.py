import MetaTrader5 as mt5

ALIASES = {
    "BTC": ["BTCUSD", "BTCUSDm", "BTCUSD.", "BTCUSD#"],
    "GOLD": ["XAUUSD", "GOLD"],
    "NASDAQ": ["USTEC", "US100", "NAS100", "USTEC.cash", "US100.cash"],
    "USDJPY": ["USDJPY", "USDJPYm"],
}


def resolve_symbol(asset_name):
    all_symbols = mt5.symbols_get()
    if all_symbols is None:
        return None

    broker_symbols = {s.name.upper(): s.name for s in all_symbols}

    for candidate in ALIASES.get(asset_name, []):
        if candidate.upper() in broker_symbols:
            return broker_symbols[candidate.upper()]

    return None