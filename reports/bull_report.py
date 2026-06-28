from pathlib import Path
from datetime import datetime

from ai.analyst_engine import AnalystEngine
from ai.bear_engine import BearEngine
from ai.bull_engine import BullEngine


analyst = AnalystEngine().generate()
bear = BearEngine().generate(analyst)
bull = BullEngine().generate(analyst, bear)

output = (
    Path("reports")
    /
    f"bull_report_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"
)

output.write_text(
    bull,
    encoding="utf-8",
)

print(output)