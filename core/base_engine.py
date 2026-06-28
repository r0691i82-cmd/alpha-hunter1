from abc import ABC, abstractmethod
from core.logger import get_logger


class BaseEngine(ABC):
    def __init__(self, name: str):
        self.name = name
        self.logger = get_logger(name)

    def run(self, data):
        self.logger.info(f"{self.name} started")

        try:
            result = self.process(data)
            self.logger.info(f"{self.name} completed")
            return result

        except Exception as e:
            self.logger.exception(f"{self.name} failed: {e}")
            return data

    @abstractmethod
    def process(self, data):
        pass