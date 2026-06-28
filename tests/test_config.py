from core.config_loader import load_settings, load_watchlist, load_indicators


def test_settings_load():
    settings = load_settings()
    assert "project" in settings
    assert "version" in settings["project"]


def test_watchlist_load():
    watchlist = load_watchlist()
    assert "watchlist" in watchlist
    assert len(watchlist["watchlist"]) > 0


def test_indicators_load():
    indicators = load_indicators()
    assert "ema_periods" in indicators
    assert 2 in indicators["ema_periods"]