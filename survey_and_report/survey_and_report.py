from survey_and_report.report import Report
from survey_and_report.survey import Survey


# Define survey answers
survey = Survey(
    q1_answer="Customer Support",
    q2_answer_1=(
            "Creating, reading, updating and deleting database entries"
        ),
    q2_answer_3="Text-based data processing",
    q2_answer_4="Retrieving data from third-party sources",
    q3_time_period=241,
    q3_unit_of_time="minutes",
    q4_yes_no_answer="I don't know"
)

# Generate report based on survey answers
report = Report(survey=survey)
report.generate()  # Outputs report text generated based on survey answers
