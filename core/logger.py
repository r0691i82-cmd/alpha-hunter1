import logging
from pathlib import Path
from datetime import datetime


def get_logger(name: str = "alpha_hunter") -> logging.Logger:
    Path("logs").mkdir(exist_ok=True)

    log_date = datetime.now().strftime("%Y-%m-%d")
    log_file = Path("logs") / f"{log_date}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger