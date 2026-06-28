from pathlib import Path
from datetime import datetime

from ai.final_decision_engine import FinalDecisionEngine


result = FinalDecisionEngine().run()

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

output = Path("reports") / f"final_decision_report_{timestamp}.md"

lines = []

lines.append("# Alpha Hunter Final Decision Report")
lines.append("")
lines.append(f"Generated: {datetime.now()}")
lines.append("")

lines.append("## Analyst Report")
lines.append("")
lines.append(result["analyst"])
lines.append("")

lines.append("## Bear Report")
lines.append("")
lines.append(result["bear"])
lines.append("")

lines.append("## Bull Report")
lines.append("")
lines.append(result["bull"])
lines.append("")

lines.append("## Risk Manager Report")
lines.append("")
lines.append(result["risk"])
lines.append("")

lines.append("## Final Judge Report")
lines.append("")
lines.append(result["judge"])
lines.append("")

output.write_text(
    "\n".join(lines),
    encoding="utf-8",
)

print(output)