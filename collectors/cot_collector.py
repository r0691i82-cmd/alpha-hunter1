from pathlib import Path
import requests
import pandas as pd

from core.base_collector import BaseCollector


COT_URL = "https://publicreporting.cftc.gov/resource/yjak-hhbj.csv?$limit=50000"


class COTCollector(BaseCollector):
    def __init__(self):
        super().__init__("cot_collector")

    def collect(self):
        Path("database/cot").mkdir(parents=True, exist_ok=True)

        self.logger.info("Downloading CFTC COT Legacy Futures Only data")

        response = requests.get(COT_URL, timeout=30)
        response.raise_for_status()

        output_file = Path("database/cot/cot_legacy_futures.csv")
        output_file.write_bytes(response.content)

        df = pd.read_csv(output_file)

        self.logger.info(f"COT rows saved: {len(df)}")
        self.logger.info(f"Saved: {output_file}")

        return True


if __name__ == "__main__":
    collector = COTCollector()
    collector.run()