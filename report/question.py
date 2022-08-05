from typing import Dict

from report.answer import Answer
from report.survey import Survey
from report.text import Text


class Question:

    def __init__(self, survey: Survey):
        self.survey = survey

    def field_of_study(self) -> str:
        answer_reports: Dict[str, str] = {
            Answer.CUSTOMER_SUPPORT: Text.CUSTOMER_SUPPORT,
            Answer.ENGINEERING_AND_TECHNICAL: Text.ENGINEERING_AND_TECHNICAL,
            Answer.PHARMACEUTICAL_AND_BIOTECHNOLOGY:
                Text.PHARMACEUTICAL_AND_BIOTECHNOLOGY,
            Answer.SCIENTIFIC_AND_ACADEMIC:
                Text.SCIENTIFIC_AND_ACADEMIC_OR_ELECTRONIC_DISCOVERY,
            Answer.ELECTRONIC_DISCOVERY:
                Text.SCIENTIFIC_AND_ACADEMIC_OR_ELECTRONIC_DISCOVERY,
        }

        return answer_reports[self.survey.FIELD_OF_STUDY]

    def required_functionality(self) -> str:
        get_third_party_data_and_process_text_data_and_crud: bool = (
            len(self.survey.REQUIRED_FUNCTIONALITY) == 3 and
            Answer.GET_THIRD_PARTY_DATA in
            self.survey.REQUIRED_FUNCTIONALITY and
            Answer.PROCESS_TEXT_BASED_DATA in
            self.survey.REQUIRED_FUNCTIONALITY and
            Answer.CRUD in self.survey.REQUIRED_FUNCTIONALITY
        )
        computations_and_get_third_party_data: bool = (
            len(self.survey.REQUIRED_FUNCTIONALITY) == 2 and
            Answer.COMPUTATIONS in self.survey.REQUIRED_FUNCTIONALITY and
            Answer.GET_THIRD_PARTY_DATA in
            self.survey.REQUIRED_FUNCTIONALITY
        )
        get_third_party_data_or_process_text_data_or_crud: bool = (
            len(self.survey.REQUIRED_FUNCTIONALITY) == 1 and
            Answer.GET_THIRD_PARTY_DATA in
            self.survey.REQUIRED_FUNCTIONALITY or
            Answer.PROCESS_TEXT_BASED_DATA in
            self.survey.REQUIRED_FUNCTIONALITY or
            Answer.CRUD in self.survey.REQUIRED_FUNCTIONALITY
        )

        if get_third_party_data_and_process_text_data_and_crud:
            return Text.GET_THIRD_PARTY_DATA_AND_PROCESS_TEXT_DATA_AND_CRUD
        elif computations_and_get_third_party_data:
            return Text.COMPUTATIONS_AND_GET_THIRD_PARTY_DATA
        elif get_third_party_data_or_process_text_data_or_crud:
            return Text.GET_THIRD_PARTY_DATA_OR_PROCESS_TEXT_DATA_OR_CRUD
        else:
            return Text.ANY_OTHER_ANSWER_COMBINATION

    def task_processing_time(self) -> str:
        time_period: int = self.survey.TASK_PROCESSING_TIME["time_period"]
        unit_of_time: str = self.survey.TASK_PROCESSING_TIME["unit_of_time"]

        if (
            time_period > 240 and unit_of_time == Answer.MINUTES
            or
            time_period > 4 and unit_of_time == Answer.HOURS
        ):
            return Text.time_more_than_240_minutes(time_period, unit_of_time)
        elif (
            time_period < 120 and unit_of_time == Answer.MINUTES
            or
            time_period < 2 and unit_of_time == Answer.HOURS
        ):
            return Text.time_less_than_120_minutes(time_period, unit_of_time)
        else:
            return Text.other_time_frames(time_period, unit_of_time)

    def do_you_work_remotely(self) -> str:
        yes_and_emails_and_live_chats: bool = (
            self.survey.DO_YOU_WORK_REMOTELY["yes_or_no_choice"] ==
            Answer.YES and
            len(self.survey.DO_YOU_WORK_REMOTELY["choices_if_yes"]) == 2 and
            Answer.EMAILS in
            self.survey.DO_YOU_WORK_REMOTELY["choices_if_yes"] and
            Answer.LIVE_CHATS in
            self.survey.DO_YOU_WORK_REMOTELY["choices_if_yes"]
        )
        yes_and_solo_data_processing_and_phone_calls: bool = (
            self.survey.DO_YOU_WORK_REMOTELY["yes_or_no_choice"] ==
            Answer.YES and
            len(self.survey.DO_YOU_WORK_REMOTELY["choices_if_yes"]) == 2 and
            Answer.SOLO_DATA_PROCESSING in
            self.survey.DO_YOU_WORK_REMOTELY["choices_if_yes"] and
            Answer.PHONE_CALLS in
            self.survey.DO_YOU_WORK_REMOTELY["choices_if_yes"]
        )

        if (self.survey.DO_YOU_WORK_REMOTELY["yes_or_no_choice"] ==
            Answer.I_DONT_KNOW
        ):
            return Text.I_DONT_KNOW
        elif (
            self.survey.DO_YOU_WORK_REMOTELY["yes_or_no_choice"] ==
            Answer.NO
        ):
            return Text.NO
        elif yes_and_emails_and_live_chats:
            return Text.YES_AND_EMAILS_AND_LIVE_CHATS
        elif yes_and_solo_data_processing_and_phone_calls:
            return Text.YES_AND_SOLO_DATA_PROCESSING_AND_PHONE_CALLS
        else:
            return Text.YES_AND_OTHER_ANSWER_COMBINATIONS
