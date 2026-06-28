from pathlib import Path
from datetime import datetime

from ai.analyst_engine import AnalystEngine


report = AnalystEngine().generate()

output = (
    Path("reports")
    /
    f"analyst_report_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"
)

output.write_text(
    report,
    encoding="utf-8",
)

print(output)