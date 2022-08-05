import unittest

from report.answer import Answer as a
from report.question import Question as q
from report.report import Report as r
from report.survey import Survey as s
from report.text import Text as t


class TestFieldOfWorkReport(unittest.TestCase):

    def test_field_of_work_report_if_customer_support(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": a.CUSTOMER_SUPPORT,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.CUSTOMER_SUPPORT
        actual_result: str = self.question.field_of_study()

        self.assertEqual(expected_result, actual_result)

    def test_field_of_work_report_if_engineering_and_technical(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": a.ENGINEERING_AND_TECHNICAL,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.ENGINEERING_AND_TECHNICAL
        actual_result: str = self.question.field_of_study()

        self.assertEqual(expected_result, actual_result)

    def test_field_of_work_report_if_pharmaceutical_and_biotechnology(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": a.PHARMACEUTICAL_AND_BIOTECHNOLOGY,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.PHARMACEUTICAL_AND_BIOTECHNOLOGY
        actual_result: str = self.question.field_of_study()

        self.assertEqual(expected_result, actual_result)

    def test_field_of_work_report_if_scientific_or_academic(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": a.SCIENTIFIC_AND_ACADEMIC,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = (
            t.SCIENTIFIC_AND_ACADEMIC_OR_ELECTRONIC_DISCOVERY
        )
        actual_result: str = self.question.field_of_study()

        self.assertEqual(expected_result, actual_result)

    def test_field_of_work_report_if_electronic_discovery(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": a.ELECTRONIC_DISCOVERY,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = (
            t.SCIENTIFIC_AND_ACADEMIC_OR_ELECTRONIC_DISCOVERY
        )
        actual_result: str = self.question.field_of_study()

        self.assertEqual(expected_result, actual_result)


class TestRequiredFunctionalityReport(unittest.TestCase):

    def test_needed_function_report_if_3rd_party_and_text_data_and_crud(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [
                    a.GET_THIRD_PARTY_DATA,
                    a.PROCESS_TEXT_BASED_DATA,
                    a.CRUD
                ],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = (
            t.GET_THIRD_PARTY_DATA_AND_PROCESS_TEXT_DATA_AND_CRUD
        )
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)

    def test_needed_function_report_if_computations_and_3rd_party_data(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [
                    a.COMPUTATIONS,
                    a.GET_THIRD_PARTY_DATA
                ],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.COMPUTATIONS_AND_GET_THIRD_PARTY_DATA
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)

    def test_needed_function_report_if_3rd_party_data(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [a.GET_THIRD_PARTY_DATA],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = (
            t.GET_THIRD_PARTY_DATA_OR_PROCESS_TEXT_DATA_OR_CRUD
        )
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)

    def test_needed_function_report_if_text_data(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [a.PROCESS_TEXT_BASED_DATA],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = (
            t.GET_THIRD_PARTY_DATA_OR_PROCESS_TEXT_DATA_OR_CRUD
        )
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)

    def test_needed_function_report_if_crud(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [a.CRUD],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = (
            t.GET_THIRD_PARTY_DATA_OR_PROCESS_TEXT_DATA_OR_CRUD
        )
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)

    def test_needed_function_report_if_any_other_answer_combination(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [a.COMPUTATIONS],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.ANY_OTHER_ANSWER_COMBINATION
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)


class TestTaskProcessinngTimeReport(unittest.TestCase):

    def test_task_processing_time_report_if_time_more_than_240_minutes(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 241,
                    "unit_of_time": a.MINUTES,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.time_more_than_240_minutes(
            time_period=241,
            unit_of_time=a.MINUTES
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)

    def test_task_processing_time_report_if_time_more_than_4_hours(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 5,
                    "unit_of_time": a.HOURS,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.time_more_than_240_minutes(
            time_period=5,
            unit_of_time=a.HOURS
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)

    def test_task_processing_time_report_if_time_less_than_120_minutes(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 119,
                    "unit_of_time": a.MINUTES,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.time_less_than_120_minutes(
            time_period=119,
            unit_of_time=a.MINUTES
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)

    def test_task_processing_time_report_if_time_less_than_2_hours(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 1,
                    "unit_of_time": a.HOURS,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.time_less_than_120_minutes(
            time_period=1,
            unit_of_time=a.HOURS
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)

    def test_task_processing_time_report_if_other_time_frames_in_minutes(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 200,
                    "unit_of_time": a.MINUTES,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.other_time_frames(
            time_period=200,
            unit_of_time=a.MINUTES
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)

    def test_task_processing_time_report_if_other_time_frames_in_hours(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 3,
                    "unit_of_time": a.HOURS,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.other_time_frames(
            time_period=3,
            unit_of_time=a.HOURS
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)


class TestDoYouWorkFromHomeReport(unittest.TestCase):

    def test_remote_work_report_if_dont_know(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": a.I_DONT_KNOW,
                    "choices_if_yes": None,
                },
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.I_DONT_KNOW
        actual_result: str = self.question.do_you_work_remotely()

        self.assertEqual(expected_result, actual_result)

    def test_remote_work_report_if_no(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": a.NO,
                    "choices_if_yes": None,
                },
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.NO
        actual_result: str = self.question.do_you_work_remotely()

        self.assertEqual(expected_result, actual_result)

    def test_remote_work_report_if_yes_and_emails_and_live_chats(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": a.YES,
                    "choices_if_yes": [a.EMAILS, a.LIVE_CHATS],
                },
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.YES_AND_EMAILS_AND_LIVE_CHATS
        actual_result: str = self.question.do_you_work_remotely()

        self.assertEqual(expected_result, actual_result)

    def test_remote_work_report_if_yes_and_solo_processing_and_phone_calls(
        self
    ):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": a.YES,
                    "choices_if_yes": [a.SOLO_DATA_PROCESSING, a.PHONE_CALLS],
                },
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.YES_AND_SOLO_DATA_PROCESSING_AND_PHONE_CALLS
        actual_result: str = self.question.do_you_work_remotely()

        self.assertEqual(expected_result, actual_result)

    def test_remote_work_report_if_yes_and_other_answer_combinations(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": a.YES,
                    "choices_if_yes": [a.SOLO_DATA_PROCESSING],
                },
            }
        )
        self.question = q(survey=survey)

        expected_result: str = t.YES_AND_OTHER_ANSWER_COMBINATIONS
        actual_result: str = self.question.do_you_work_remotely()

        self.assertEqual(expected_result, actual_result)


class TestOverallReport(unittest.TestCase):

    def test_overall_report_generation(self):
        survey = s(
            answers={
                "FIELD_OF_STUDY": a.CUSTOMER_SUPPORT,
                "REQUIRED_FUNCTIONALITY": [
                    a.GET_THIRD_PARTY_DATA,
                    a.PROCESS_TEXT_BASED_DATA,
                    a.CRUD
                ],
                "TASK_PROCESSING_TIME": {
                    "time_period": 241,
                    "unit_of_time": a.MINUTES,
                },
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": a.YES,
                    "choices_if_yes": [a.EMAILS, a.LIVE_CHATS]
                },
            }
        )
        task_processing_time_report: str = (
            t.time_more_than_240_minutes(
                time_period=241, unit_of_time=a.MINUTES
            )
        )

        expected_result: str = (
            f"{t.CUSTOMER_SUPPORT}\n\n"
            f"{t.GET_THIRD_PARTY_DATA_AND_PROCESS_TEXT_DATA_AND_CRUD}\n\n"
            f"{task_processing_time_report}\n\n"
            f"{t.YES_AND_EMAILS_AND_LIVE_CHATS}\n\n"
        )
        actual_result: str = r(survey=survey).generate()

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
