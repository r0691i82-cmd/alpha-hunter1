from pathlib import Path
from datetime import datetime

from ai.report_generator import AIReportGenerator


report = AIReportGenerator().generate_offline_report()

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
output_file = Path("reports") / f"ai_institutional_report_{timestamp}.md"

output_file.write_text(report, encoding="utf-8")

print(f"AI Institutional Report Saved: {output_file}")