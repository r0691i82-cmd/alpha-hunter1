from abc import ABC, abstractmethod
from core.logger import get_logger


class BaseCollector(ABC):
    def __init__(self, name: str):
        self.name = name
        self.logger = get_logger(name)

    def run(self):
        self.logger.info(f"{self.name} started")

        try:
            result = self.collect()
            self.logger.info(f"{self.name} completed")
            return result

        except Exception as e:
            self.logger.exception(f"{self.name} failed: {e}")
            return None

    @abstractmethod
    def collect(self):
        pass