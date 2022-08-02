class Survey:

    Q1 = "Which field are you working in?"
    Q2 = "Which functionality would be helpful in your line of work?"
    Q3 = "How long on average does it take you to process one request/task?"
    Q4 = "Do you work remotely (from home)?"

    def __init__(
            self,
            q1_answer: str = None,
            q2_answer_1: str = None,
            q2_answer_2: str = None,
            q2_answer_3: str = None,
            q2_answer_4: str = None,
            q3_time_period: int = None,
            q3_unit_of_time: str = None,
            q4_yes_no_answer: str = None,
            q4_yes_option_1: str = None,
            q4_yes_option_2: str = None,
            q4_yes_option_3: str = None,
            q4_yes_option_4: str = None

    ):
        self.q1_answer = q1_answer
        self.q2_answer_1 = q2_answer_1
        self.q2_answer_2 = q2_answer_2
        self.q2_answer_3 = q2_answer_3
        self.q2_answer_4 = q2_answer_4
        self.q3_time_period = q3_time_period
        self.q3_unit_of_time = q3_unit_of_time
        self.q4_yes_no_answer = q4_yes_no_answer
        self.q4_yes_option_1 = q4_yes_option_1
        self.q4_yes_option_2 = q4_yes_option_2
        self.q4_yes_option_3 = q4_yes_option_3
        self.q4_yes_option_4 = q4_yes_option_4
