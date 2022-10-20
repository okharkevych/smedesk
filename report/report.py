from typing import List

from report.question import Question
from report.survey import Survey


class Report:

    def __init__(self, survey: Survey):
        self.question = Question(survey=survey)

    def generate(self) -> str:
        report: str = ""

        field_of_study: str = self.question.field_of_study()
        required_functionality: str = self.question.required_functionality()
        task_processing_time: str = self.question.task_processing_time()
        do_you_work_remotely: str = self.question.do_you_work_remotely()

        report_parts: List[str] = [
            field_of_study,
            required_functionality,
            task_processing_time,
            do_you_work_remotely
        ]

        for report_part in report_parts:
            report += f"{report_part}\n\n"

        return report
