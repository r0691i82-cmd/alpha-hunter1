from pathlib import Path
from datetime import datetime

from ai.analyst_engine import AnalystEngine
from ai.bear_engine import BearEngine
from ai.bull_engine import BullEngine
from ai.risk_manager_engine import RiskManagerEngine


analyst = AnalystEngine().generate()

bear = BearEngine().generate(
    analyst,
)

bull = BullEngine().generate(
    analyst,
    bear,
)

risk = RiskManagerEngine().generate(
    analyst,
    bear,
    bull,
)

output = (
    Path("reports")
    /
    f"risk_manager_report_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"
)

output.write_text(
    risk,
    encoding="utf-8",
)

print(output)