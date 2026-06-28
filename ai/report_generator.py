from ai.prompt_builder import InstitutionalPromptBuilder


class AIReportGenerator:
    def generate_offline_report(self):
        prompt = InstitutionalPromptBuilder().build()

        report = f"""
# Alpha Hunter AI Institutional Report

## Mode
Offline Draft Report

## Notice
This report is generated without external LLM API calls.
It uses the structured prompt context prepared for Gemini/Grok.

## Institutional Analysis Prompt

{prompt}
"""
        return report.strip()