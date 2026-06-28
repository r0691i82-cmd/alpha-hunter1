from core.config_loader import load_settings, load_watchlist, load_indicators
from core.logger import get_logger


logger = get_logger("main")

settings = load_settings()
watchlist = load_watchlist()
indicators = load_indicators()

print("=" * 60)
print("Alpha Hunter v2.0.0 Foundation")
print("=" * 60)
print("Project:", settings["project"]["name"])
print("Version:", settings["project"]["version"])
print("Watchlist:", watchlist["watchlist"])
print("EMA:", indicators["ema_periods"])
print("=" * 60)

logger.info("Alpha Hunter Foundation Boot OK")