import json

from ai.ai_context_builder import AIContextBuilder


context = AIContextBuilder().build()

print(json.dumps(context, indent=2, ensure_ascii=False))