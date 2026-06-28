from pathlib import Path
from datetime import datetime

from ai.gemini_engine import GeminiEngine

report = GeminiEngine().generate()

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

output = Path("reports") / f"gemini_report_{timestamp}.md"

output.write_text(
    report,
    encoding="utf-8",
)

print(output)