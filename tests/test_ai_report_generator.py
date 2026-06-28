from ai.report_generator import AIReportGenerator


def test_ai_report_generator_runs():
    report = AIReportGenerator().generate_offline_report()

    assert report is not None
    assert "Alpha Hunter AI Institutional Report" in report
    assert "Institutional Analysis Prompt" in report