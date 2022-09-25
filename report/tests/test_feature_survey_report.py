import unittest

from report.answer import Answer
from report.question import Question
from report.report import Report
from report.survey import Survey
from report.text import Text


class TestFieldOfWorkReport(unittest.TestCase):

    def test_field_of_work_report_if_customer_support(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": Answer.CUSTOMER_SUPPORT,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.CUSTOMER_SUPPORT
        actual_result: str = self.question.field_of_study()

        self.assertEqual(expected_result, actual_result)

    def test_field_of_work_report_if_engineering_and_tech(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": Answer.ENGINEERING_AND_TECH,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.ENGINEERING_AND_TECH
        actual_result: str = self.question.field_of_study()

        self.assertEqual(expected_result, actual_result)

    def test_field_of_work_report_if_pharm_and_bio(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": Answer.PHARM_AND_BIO,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.PHARM_AND_BIO
        actual_result: str = self.question.field_of_study()

        self.assertEqual(expected_result, actual_result)

    def test_field_of_work_report_if_scientific_or_academic(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": Answer.SCIENTIFIC_AND_ACADEMIC,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = (
            Text.SCIENCE_OR_LAW
        )
        actual_result: str = self.question.field_of_study()

        self.assertEqual(expected_result, actual_result)

    def test_field_of_work_report_if_electronic_discovery(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": Answer.ELECTRONIC_DISCOVERY,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = (
            Text.SCIENCE_OR_LAW
        )
        actual_result: str = self.question.field_of_study()

        self.assertEqual(expected_result, actual_result)


class TestRequiredFunctionalityReport(unittest.TestCase):

    def test_needed_function_report_if_3rd_party_and_text_data_and_crud(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [
                    Answer.GET_THIRD_PARTY_DATA,
                    Answer.PROCESS_TEXT_BASED_DATA,
                    Answer.CRUD
                ],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = (
            Text.GET_DATA_PROCESS_TEXT_AND_CRUD
        )
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)

    def test_needed_function_report_if_computations_and_3rd_party_data(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [
                    Answer.COMPUTATIONS,
                    Answer.GET_THIRD_PARTY_DATA
                ],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.COMPUTATIONS_AND_GET_DATA
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)

    def test_needed_function_report_if_3rd_party_data(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [Answer.GET_THIRD_PARTY_DATA],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = (
            Text.GET_DATA_OR_PROCESS_TEXT_OR_CRUD
        )
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)

    def test_needed_function_report_if_text_data(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [Answer.PROCESS_TEXT_BASED_DATA],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = (
            Text.GET_DATA_OR_PROCESS_TEXT_OR_CRUD
        )
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)

    def test_needed_function_report_if_crud(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [Answer.CRUD],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = (
            Text.GET_DATA_OR_PROCESS_TEXT_OR_CRUD
        )
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)

    def test_needed_function_report_if_any_other_answer_combination(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": [Answer.COMPUTATIONS],
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.ANY_OTHER_ANSWER_COMBINATION
        actual_result: str = self.question.required_functionality()

        self.assertEqual(expected_result, actual_result)


class TestTaskProcessinngTimeReport(unittest.TestCase):

    def test_task_processing_time_report_if_time_more_than_240_minutes(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 241,
                    "unit_of_time": Answer.MINUTES,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.time_more_than_240_minutes(
            time_period=241,
            unit_of_time=Answer.MINUTES
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)

    def test_task_processing_time_report_if_time_more_than_4_hours(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 5,
                    "unit_of_time": Answer.HOURS,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.time_more_than_240_minutes(
            time_period=5,
            unit_of_time=Answer.HOURS
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)

    def test_task_processing_time_report_if_time_less_than_120_minutes(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 119,
                    "unit_of_time": Answer.MINUTES,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.time_less_than_120_minutes(
            time_period=119,
            unit_of_time=Answer.MINUTES
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)

    def test_task_processing_time_report_if_time_less_than_2_hours(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 1,
                    "unit_of_time": Answer.HOURS,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.time_less_than_120_minutes(
            time_period=1,
            unit_of_time=Answer.HOURS
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)

    def test_task_processing_time_report_if_other_time_frames_in_minutes(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 200,
                    "unit_of_time": Answer.MINUTES,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.other_time_frames(
            time_period=200,
            unit_of_time=Answer.MINUTES
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)

    def test_task_processing_time_report_if_other_time_frames_in_hours(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": {
                    "time_period": 3,
                    "unit_of_time": Answer.HOURS,
                },
                "DO_YOU_WORK_REMOTELY": None,
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.other_time_frames(
            time_period=3,
            unit_of_time=Answer.HOURS
        )
        actual_result: str = self.question.task_processing_time()

        self.assertEqual(expected_result, actual_result)


class TestDoYouWorkFromHomeReport(unittest.TestCase):

    def test_remote_work_report_if_dont_know(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": Answer.I_DONT_KNOW,
                    "choices_if_yes": None,
                },
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.I_DONT_KNOW
        actual_result: str = self.question.do_you_work_remotely()

        self.assertEqual(expected_result, actual_result)

    def test_remote_work_report_if_no(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": Answer.NO,
                    "choices_if_yes": None,
                },
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.NO
        actual_result: str = self.question.do_you_work_remotely()

        self.assertEqual(expected_result, actual_result)

    def test_remote_work_report_if_yes_and_emails_and_live_chats(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": Answer.YES,
                    "choices_if_yes": [Answer.EMAILS, Answer.LIVE_CHATS],
                },
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.YES_AND_EMAILS_AND_LIVE_CHATS
        actual_result: str = self.question.do_you_work_remotely()

        self.assertEqual(expected_result, actual_result)

    def test_remote_work_report_if_yes_and_solo_processing_and_phone_calls(
        self
    ):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": Answer.YES,
                    "choices_if_yes": [
                        Answer.SOLO_DATA_PROCESSING,
                        Answer.PHONE_CALLS
                    ],
                },
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.YES_AND_SOLO_WORK_AND_PHONE_CALLS
        actual_result: str = self.question.do_you_work_remotely()

        self.assertEqual(expected_result, actual_result)

    def test_remote_work_report_if_yes_and_other_answer_combinations(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": None,
                "REQUIRED_FUNCTIONALITY": None,
                "TASK_PROCESSING_TIME": None,
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": Answer.YES,
                    "choices_if_yes": [Answer.SOLO_DATA_PROCESSING],
                },
            }
        )
        self.question = Question(survey=survey)

        expected_result: str = Text.YES_AND_OTHER_ANSWER_COMBINATIONS
        actual_result: str = self.question.do_you_work_remotely()

        self.assertEqual(expected_result, actual_result)


class TestOverallReport(unittest.TestCase):

    def test_overall_report_generation(self):
        survey = Survey(
            answers={
                "FIELD_OF_STUDY": Answer.CUSTOMER_SUPPORT,
                "REQUIRED_FUNCTIONALITY": [
                    Answer.GET_THIRD_PARTY_DATA,
                    Answer.PROCESS_TEXT_BASED_DATA,
                    Answer.CRUD
                ],
                "TASK_PROCESSING_TIME": {
                    "time_period": 241,
                    "unit_of_time": Answer.MINUTES,
                },
                "DO_YOU_WORK_REMOTELY": {
                    "yes_or_no_choice": Answer.YES,
                    "choices_if_yes": [Answer.EMAILS, Answer.LIVE_CHATS]
                },
            }
        )
        task_processing_time_report: str = (
            Text.time_more_than_240_minutes(
                time_period=241, unit_of_time=Answer.MINUTES
            )
        )

        expected_result: str = (
            f"{Text.CUSTOMER_SUPPORT}\n\n"
            f"{Text.GET_DATA_PROCESS_TEXT_AND_CRUD}\n\n"
            f"{task_processing_time_report}\n\n"
            f"{Text.YES_AND_EMAILS_AND_LIVE_CHATS}\n\n"
        )
        actual_result: str = Report(survey=survey).generate()

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
