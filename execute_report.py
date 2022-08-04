from report.answer import Answer
from report.report import Report
from report.survey import Survey

survey = Survey(
    answers={
        "FIELD_OF_STUDY": Answer.CUSTOMER_SUPPORT,
        "REQUIRED_FUNCTIONALITY": [
            Answer.CRUD,
            Answer.PROCESS_TEXT_BASED_DATA,
            Answer.GET_THIRD_PARTY_DATA
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

report = Report(survey=survey)
report.generate()
