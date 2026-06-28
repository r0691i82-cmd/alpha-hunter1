from pathlib import Path
from datetime import datetime

from ai.analyst_engine import AnalystEngine
from ai.bear_engine import BearEngine

analyst = AnalystEngine().generate()

bear = BearEngine().generate(analyst)

output = (
    Path("reports")
    /
    f"bear_report_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"
)

output.write_text(
    bear,
    encoding="utf-8",
)

print(output)