from pathlib import Path
from datetime import datetime

from ai.analyst_engine import AnalystEngine
from ai.bear_engine import BearEngine
from ai.bull_engine import BullEngine
from ai.risk_manager_engine import RiskManagerEngine
from ai.judge_engine import JudgeEngine


analyst = AnalystEngine().generate()
bear = BearEngine().generate(analyst)
bull = BullEngine().generate(analyst, bear)
risk = RiskManagerEngine().generate(analyst, bear, bull)
judge = JudgeEngine().generate(analyst, bear, bull, risk)

output = (
    Path("reports")
    /
    f"judge_report_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"
)

output.write_text(
    judge,
    encoding="utf-8",
)

print(output)