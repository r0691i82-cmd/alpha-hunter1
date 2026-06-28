from pathlib import Path
import yaml


CONFIG_DIR = Path("config")


def load_yaml(filename: str) -> dict:
    path = CONFIG_DIR / filename

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_settings() -> dict:
    return load_yaml("settings.yaml")


def load_watchlist() -> dict:
    return load_yaml("watchlist.yaml")


def load_indicators() -> dict:
    return load_yaml("indicators.yaml")