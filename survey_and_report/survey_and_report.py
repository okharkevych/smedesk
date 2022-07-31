from typing import Dict, List, Union


class Survey:

    Q1 = "Which field are you working in?"
    Q2 = "Which functionality would be helpful in your line of work?"
    Q3 = "How long on average does it take you to process one request/task?"
    Q4 = "Do you work remotely (from home)?"

    def __init__(
            self,
            q1_answer: str,
            q2_answer_1: str = None,
            q2_answer_2: str = None,
            q2_answer_3: str = None,
            q2_answer_4: str = None,
            q3_time_period: int = None,
            q3_unit_of_time: str = None,
            q4_yes_no_answer: str = None,
            **q4_yes_options: str
    ):
        self.q1_answer = q1_answer
        self.q2_answer_1 = q2_answer_1
        self.q2_answer_2 = q2_answer_2
        self.q2_answer_3 = q2_answer_3
        self.q2_answer_4 = q2_answer_4
        self.q3_time_period = q3_time_period
        self.q3_unit_of_time = q3_unit_of_time
        self.q4_yes_no_answer = q4_yes_no_answer

        self.__dict__.update(q4_yes_options)


class AnswerType:

    ANSWER_1: int = 0
    ANSWER_2: int = 1
    ANSWER_3: int = 2
    ANSWER_4: int = 3
    ANSWER_5: int = 4

    ANSWER_I_DONT_KNOW: int = 5
    ANSWER_NO: int = 6
    ANSWER_YES: int = 7
    ANSWER_YES_CHOICE_1: int = 8
    ANSWER_YES_CHOICE_2: int = 9
    ANSWER_YES_CHOICE_3: int = 10
    ANSWER_YES_CHOICE_4: int = 11


class ReportOptions:

    q1: Dict[str, Dict[Union[int, str], str]] = {
        "answer_options": {
            AnswerType.ANSWER_1: "Customer Support",
            AnswerType.ANSWER_2: "Engineering and technical fields",
            AnswerType.ANSWER_3: "Pharmaceutical and biotechnology areas",
            AnswerType.ANSWER_4: "Scientific and academic fields",
            AnswerType.ANSWER_5: "Electronic discovery",
        },
        "reports": {
            "report_1": (
                "Lorem ipsum 1. Question - ANSWER_1 dolor sit amet, "
                "consectetur adipiscing elit. Mauris sed ligula vitae tellus "
                "pellentesque vehicula nec eu velit. Curabitur luctus et nibh "
                "et ornare. Suspendisse non mattis lacus. Cras vitae mi "
                "ornare, euismod velit sit amet, iaculis tortor. In tempor "
                "purus sapien.\n\nDonec tincidunt 1. Question - ANSWER_1 metus"
                " nec dui tristique malesuada. Praesent lectus nunc, accumsan "
                "vel justo in, imperdiet faucibus leo. Nullam efficitur massa "
                "nec turpis tincidunt, feugiat viverra erat rutrum. Aliquam "
                "eget auctor lectus, mollis blandit ipsum. Phasellus maximus "
                "finibus arcu a tincidunt."
            ),
            "report_2": (
                "Lorem ipsum 1. Question - ANSWER_2 dolor sit amet, "
                "consectetur adipiscing elit. Ut et augue id leo egestas "
                "interdum in eu lectus. Aliquam vel finibus nisi. Vestibulum "
                "mattis sagittis lectus sed pulvinar. Sed aliquam felis "
                "tortor, sed scelerisque nibh cursus sit amet. Donec a "
                "sollicitudin nisi. Mauris non enim ac felis lobortis commodo."
                " Sed laoreet tellus non felis rutrum, in hendrerit ipsum "
                "porta. Sed quis sem velit."
            ),
            "report_3": (
                "Sed vel bibendum tortor. Proin a aliquet tortor. Vivamus "
                "rhoncus 1. Question - ANSWER_3 risus nec ultricies rutrum. "
                "Mauris bibendum lectus risus, non porttitor urna interdum "
                "quis.\n\nSuspendisse quis risus scelerisque, 1. Question - "
                "ANSWER_3 feugiat augue nec, semper leo. Fusce euismod "
                "facilisis mi, tristique sollicitudin metus hendrerit non. "
                "Nulla ac sodales quam, sit amet finibus metus. Ut in felis "
                "tellus. Sed aliquet metus ullamcorper est vestibulum mattis. "
                "Cras nisi sem, euismod in egestas vel, ullamcorper ac sapien."
                " In porttitor elementum faucibus."
            ),
            "report_4": (
                "Mauris urna nunc, eleifend id sapien eget, tincidunt "
                "venenatis risus. Vestibulum imperdiet enim at nibh sodales, "
                "1. Question - ANSWER_4 or ANSWER_5 or ANSWER_6 eget "
                "scelerisque odio finibus.\n\nNullam ut mi eget sapien "
                "accumsan iaculis. Vestibulum in maximus metus, 1. Question - "
                "ANSWER_4 or ANSWER_5 or ANSWER_6 vitae venenatis sapien. "
                "Nullam auctor odio vehicula, posuere elit in, ullamcorper "
                "lectus. Mauris pharetra dapibus congue. Suspendisse potenti."
            ),
        },
    }

    q2: Dict[str, Dict[Union[int, str], str]] = {
        "answer_options": {
            AnswerType.ANSWER_1: (
                "Creating, reading, updating and deleting database entries"
            ),
            AnswerType.ANSWER_2: "Computations",
            AnswerType.ANSWER_3: "Text-based data processing",
            AnswerType.ANSWER_4: "Retrieving data from third-party sources",
        },
        "reports": {
            "report_1": (
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed "
                "sollicitudin leo in 2. Question - ANSWER_4, ANSWER_3 and "
                "ANSWER_1 lectus cursus tincidunt. Nullam dapibus tincidunt "
                "libero nec volutpat.\n\nCras sit amet massa a turpis "
                "malesuada ornare vitae sed arcu. Maecenas eleifend rutrum "
                "augue, eget imperdiet sem gravida sed. Vestibulum vel libero "
                "consectetur, 2. Question - ANSWER_4, ANSWER_3 and ANSWER_1 "
                "pellentesque lacus nec, facilisis nisl. Phasellus faucibus "
                "lobortis tincidunt. Duis tristique congue bibendum.\n\nMorbi "
                "semper cursus felis et consequat. Nulla posuere, quam eget "
                "pulvinar 2. Question - ANSWER_4, ANSWER_3 and ANSWER_1 "
                "dignissim, odio sem euismod leo, at ornare purus massa quis "
                "sapien. Aliquam eget libero nec lectus placerat congue. "
                "Aenean nec tortor a ligula aliquam pharetra. Aenean et magna "
                "enim."
            ),
            "report_2": (
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                "Vestibulum dictum, dui non auctor tristique, odio sem 2. "
                "Question - ANSWER_2 and ANSWER_4 convallis lacus, non gravida"
                " libero erat id justo. Praesent in varius nisi. Phasellus "
                "suscipit elit sit amet aliquam tincidunt.\n\nIn pellentesque "
                "gravida risus, et 2. Question - ANSWER_2 and ANSWER_4 rhoncus"
                " quam. Vestibulum ac risus nulla. Phasellus iaculis interdum "
                "pulvinar. Vivamus sit amet sagittis risus. Morbi ut "
                "pellentesque sapien."
            ),
            "report_3": (
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras"
                " viverra luctus nunc, non ultrices mauris molestie vitae. Sed"
                " gravida purus finibus 2. Question - ANSWER_4, ANSWER_3 or "
                "ANSWER_1 efficitur congue. Vestibulum magna urna, volutpat "
                "vitae auctor non, pharetra vel leo.\n\nInterdum et malesuada "
                "fames ac ante ipsum primis in faucibus. Vestibulum elementum "
                "sagittis tortor, vel porta leo tristique ac. Phasellus ac "
                "metus est. 2. Question - ANSWER_4, ANSWER_3 or ANSWER_1 "
                "Aenean vel malesuada ex, nec rutrum justo. Sed ultricies "
                "venenatis mauris, in pharetra ante vulputate nec. Proin "
                "viverra convallis augue elementum volutpat."
            ),
            "report_4": (
                "Consectetur adipiscing elit, sed do eiusmod tempor incididunt"
                " ut labore et dolore magna aliqua. Ut enim ad minim veniam, "
                "quis nostrud exercitation ullamco laboris nisi ut aliquip ex "
                "ea commodo consequat.\n\nDuis aute irure dolor in "
                "reprehenderit in voluptate velit esse cillum dolore eu fugiat"
                " nulla pariatur. Excepteur sint occaecat cupidatat non "
                "proident, sunt in culpa qui officia deserunt mollit anim id "
                "est laborum."
            ),
        },
    }

    q3: Dict[str, str] = {
        "report_1": (
            f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            f"Calories: ..... Vivamus hendrerit arcu eros, nec bibendum mi sodales id. Ut auctor nisl a placerat porttitor. Duis at tortor posuere, gravida sapien in, fermentum ligula.\n\nQuisque eu ipsum lobortis, hendrerit justo vitae, varius nisi. Etiam in leo feugiat purus facilisis tempor. Fusce congue metus non massa mollis, id imperdiet ex viverra. Cras Calories: ..... imperdiet lectus at imperdiet ornare."
        ),
        "report_2": (
            f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer porta at odio ac rhoncus. Calories: ..... Integer viverra porta eros nec ultrices. Nullam ante sem, tincidunt vitae orci id, vestibulum auctor risus. Phasellus sit amet lobortis eros. Maecenas convallis dolor ex, vel congue ipsum ornare eu.\n\nNunc in mattis dolor, quis posuere lorem. Calories: ..... Nullam condimentum semper diam, lacinia tempor eros tristique ut. Etiam ultrices imperdiet tortor at eleifend. Aenean lorem felis, volutpat eu euismod at, congue id erat. Duis luctus quam vitae mattis tempus."
        ),
        "report_3": (
            f"Sed at aliquam ex. Vestibulum maximus erat in justo maximus posuere. Calories: ..... Suspendisse tellus magna, faucibus scelerisque dapibus et, luctus egestas nibh. Pellentesque eleifend mauris ac volutpat ullamcorper.\n\nAenean vitae velit et nulla egestas viverra sit amet eu eros. Calories: ..... Nunc congue rutrum sem"
        ),
    }


class Report:

    def __init__(self, survey: Survey):
        self.survey = survey

    def q1_report(self) -> str:
        answer_reports: Dict[str, str] = {
            ReportOptions.q1["answer_options"][AnswerType.ANSWER_1]: (
                ReportOptions.q1["reports"]["report_1"]
            ),
            ReportOptions.q1["answer_options"][AnswerType.ANSWER_2]: (
                ReportOptions.q1["reports"]["report_2"]
            ),
            ReportOptions.q1["answer_options"][AnswerType.ANSWER_3]: (
                ReportOptions.q1["reports"]["report_3"]
            ),
            ReportOptions.q1["answer_options"][AnswerType.ANSWER_4]: (
                ReportOptions.q1["reports"]["report_4"]
            ),
            ReportOptions.q1["answer_options"][AnswerType.ANSWER_5]: (
                ReportOptions.q1["reports"]["report_4"]
            ),
        }

        return answer_reports[self.survey.q1_answer]

    def q2_report(self) -> str:
        if (
                not self.survey.q2_answer_2
                and (
                self.survey.q2_answer_1
                == ReportOptions.q2["answer_options"][AnswerType.ANSWER_1]
                )
                and (
                self.survey.q2_answer_3
                == ReportOptions.q2["answer_options"][AnswerType.ANSWER_3]
                )
                and (
                self.survey.q2_answer_4
                == ReportOptions.q2["answer_options"][AnswerType.ANSWER_4]
                )
        ):
            report: str = ReportOptions.q2["reports"]["report_1"]
        elif (
                not any([self.survey.q2_answer_1, self.survey.q2_answer_3])
                and (
                self.survey.q2_answer_2
                == ReportOptions.q2["answer_options"][AnswerType.ANSWER_2]
                )
                and (
                self.survey.q2_answer_4
                == ReportOptions.q2["answer_options"][AnswerType.ANSWER_4]
                )
        ):
            report: str = ReportOptions.q2["reports"]["report_2"]
        elif (
                not self.survey.q2_answer_2
                and (
                        (
                            self.survey.q2_answer_1
                            == ReportOptions.q2["answer_options"][
                                AnswerType.ANSWER_1
                            ]
                            and not any([
                                self.survey.q2_answer_3,
                                self.survey.q2_answer_4
                            ])
                        )
                        or (
                                (
                                    self.survey.q2_answer_3
                                    == ReportOptions.q2["answer_options"][
                                        AnswerType.ANSWER_3
                                    ]
                                    and not any([
                                        self.survey.q2_answer_1,
                                        self.survey.q2_answer_4
                                    ])
                                )
                        )
                        or (
                                (
                                    self.survey.q2_answer_4
                                    == ReportOptions.q2["answer_options"][
                                        AnswerType.ANSWER_4
                                    ]
                                    and not any([
                                        self.survey.q2_answer_1,
                                        self.survey.q2_answer_3
                                    ])
                                )
                        )
                )
        ):
            report: str = ReportOptions.q2["reports"]["report_3"]
        else:
            report: str = ReportOptions.q2["reports"]["report_4"]

        return report

    def q3_report(self) -> str:
        pass

    def q4_report(self) -> str:
        pass

    def generate(self) -> str:
        pass


survey_1 = Survey(
    q1_answer="Customer Support",
    q2_answer_1="Creating, reading, updating and deleting database entries",
    # q2_answer_2="Computations",
    q2_answer_3="Text-based data processing",
    q2_answer_4="Retrieving data from third-party sources",
    q3_time_period=0,
    q3_unit_of_time="",
    q4_yes_no_answer="",
    # q4_yes_options="",
)

report_1 = Report(survey=survey_1)

assert report_1.q1_report() == ReportOptions().q1["reports"]["report_1"]
assert report_1.q2_report() == ReportOptions().q2["reports"]["report_1"]
breakpoint()


def question_3(time_period: int, unit_of_time: str) -> str:
    all_reports: Dict[str, str] = {
        "report_1": f"Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    f" Recommended shift duration: "
                    f"{round(time_period * 1.5, 1)} {unit_of_time} Vivamus "
                    f"hendrerit "
                    f"arcu eros, nec bibendum mi sodales id. Ut auctor nisl a "
                    f"placerat porttitor. Duis at tortor posuere, gravida "
                    f"sapien in, fermentum ligula.\n\nQuisque eu ipsum "
                    f"lobortis, hendrerit justo vitae, varius nisi. Etiam in "
                    f"leo feugiat purus facilisis tempor. Fusce congue metus "
                    f"non massa mollis, id imperdiet ex viverra. Cras "
                    f"Recommended shift duration: "
                    f"{round(time_period * 1.5, 1)} {unit_of_time} imperdiet "
                    f"lectus at "
                    f"imperdiet ornare.",
        "report_2": f"Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    f" Integer porta at odio ac rhoncus. "
                    f"Recommended shift duration: "
                    f"{round(time_period * 1.5 * 3.5, 1)} {unit_of_time} "
                    f"Integer viverra porta "
                    f"eros nec ultrices. Nullam ante sem, tincidunt vitae orci"
                    f" id, vestibulum auctor risus. Phasellus sit amet "
                    f"lobortis eros. Maecenas convallis dolor ex, vel congue "
                    f"ipsum ornare eu.\n\nNunc in mattis dolor, quis posuere "
                    f"lorem. Recommended shift duration: "
                    f"{round(time_period * 1.5 * 3.5, 1)} {unit_of_time} "
                    f"Nullam "
                    f"condimentum semper diam, lacinia tempor eros tristique "
                    f"ut. Etiam ultrices imperdiet tortor at eleifend. Aenean "
                    f"lorem felis, volutpat eu euismod at, congue id erat. "
                    f"Duis luctus quam vitae mattis tempus.",
        "report_3": f"Sed at aliquam ex. Vestibulum maximus erat in justo "
                    f"maximus posuere. Recommended shift duration: "
                    f"{round(time_period * 1.5 * 2.67, 1)} {unit_of_time} "
                    f"Suspendisse tellus magna, faucibus scelerisque dapibus "
                    f"et, luctus egestas nibh. Pellentesque eleifend mauris ac"
                    f" volutpat ullamcorper.\n\nAenean vitae velit et nulla "
                    f"egestas viverra sit amet eu eros. "
                    f"Recommended shift duration: "
                    f"{round(time_period * 1.5 * 2.67, 1)} {unit_of_time} Nunc"
                    f" congue rutrum sem"
    }

    if (
            (time_period > 240 and unit_of_time == "minutes")
            or (time_period > 4 and unit_of_time == "hours")
    ):
        report: str = all_reports["report_1"]
    elif (
            (time_period < 120 and unit_of_time == "minutes")
            or (time_period < 2 and unit_of_time == "hours")
    ):
        report: str = all_reports["report_2"]
    else:
        report: str = all_reports["report_3"]

    return report


def question_4(answer_1: str, **answers_yes: str) -> str:
    answer_1_options: Dict[int, str] = {
        ANSWER_YES: "Yes",
        ANSWER_NO: "No",
        ANSWER_I_DONT_KNOW: "I don't know",
    }

    answer_yes_options: Dict[int, str] = {
        ANSWER_YES_CHOICE_1: (
            "Gathering and processing data, developing solutions by yourself"
        ),
        ANSWER_YES_CHOICE_2: "Email correspondence",
        ANSWER_YES_CHOICE_3: "Live chat correspondence",
        ANSWER_YES_CHOICE_4: "Phone calls",
    }

    all_reports: Dict[str, str] = {
        "report_dont_know": "Phasellus ac sem ornare, ANSWER_I_DONT_KNOW "
                            "euismod tellus id, sagittis felis. Nullam viverra"
                            " est nibh, et dignissim elit tincidunt nec. "
                            "Integer vel dolor aliquam, eleifend metus in, "
                            "tincidunt erat. Nam id facilisis tortor.\n\nDonec"
                            " malesuada, libero nec tincidunt "
                            "ANSWER_I_DONT_KNOW commodo, nulla velit imperdiet"
                            " mauris, sit amet cursus dui quam maximus justo. "
                            "In accumsan nisi ut orci finibus ullamcorper. "
                            "Aliquam consequat risus non orci dapibus, id "
                            "commodo erat egestas.",
        "report_no": "Nam maximus et massa laoreet congue. In facilisis "
                     "egestas neque. Nullam ac euismod nibh. ANSWER_NO Aenean "
                     "pulvinar lacinia ligula, nec lobortis magna accumsan "
                     "sed.\n\nDuis tempor pellentesque quam. ANSWER_NO Sed non"
                     " est dui. Sed commodo odio vel augue pellentesque, et "
                     "sagittis dolor tristique. Phasellus mollis magna eu "
                     "egestas viverra. Cras elementum erat vel libero "
                     "venenatis, ut suscipit nibh scelerisque.",
        "report_yes_2_3": "Mauris viverra lobortis ante, eget faucibus felis "
                          "pulvinar et. Suspendisse urna diam, ANSWER_YES and "
                          "ANSWER_YES_CHOICE_2, ANSWER_YES_CHOICE_3 elementum "
                          "nec tincidunt ornare, convallis condimentum nisi."
                          "\n\nNam gravida ac magna eget cursus. ANSWER_YES "
                          "and ANSWER_YES_CHOICE_2, ANSWER_YES_CHOICE_3 "
                          "Maecenas fermentum lacus eu tempor condimentum. "
                          "Quisque tristique viverra justo, et mollis magna "
                          "ornare a. In lacus elit, vestibulum a ex facilisis,"
                          " faucibus gravida dui. Morbi consectetur egestas "
                          "tempor. Sed neque ex, condimentum congue facilisis "
                          "non, aliquet sed odio.",
        "report_yes_1_4": "Fusce sem est, maximus ac efficitur in, accumsan eu"
                          " libero. Praesent facilisis, augue at pretium "
                          "malesuada, ANSWER_YES and ANSWER_YES_CHOICE_1, "
                          "ANSWER_YES_CHOICE_4 erat eros eleifend velit, at "
                          "iaculis nunc nisi nec odio. Ut consequat ac metus a"
                          " bibendum. Donec venenatis euismod eros ac "
                          "dignissim. Donec dictum odio a augue tincidunt "
                          "interdum.",
        "report_yes_other": "Lorem ipsum dolor sit amet, consectetur "
                            "adipiscing elit. Pellentesque sed scelerisque "
                            "nulla, at mattis mauris. Vestibulum dignissim "
                            "viverra nulla quis tempus. (Any other case)\n"
                            "Donec finibus nisl sapien, sed auctor elit "
                            "sodales ac. Nulla dictum ante ante, eget maximus "
                            "mi efficitur nec.",
    }

    if answer_1 == answer_1_options[ANSWER_I_DONT_KNOW]:
        report: str = all_reports["report_dont_know"]
    elif answer_1 == answer_1_options[ANSWER_NO]:
        report: str = all_reports["report_no"]
    else:
        if (
            len(answers_yes) == 2
            and answer_yes_options[ANSWER_YES_CHOICE_2] in answers_yes.values()
            and answer_yes_options[ANSWER_YES_CHOICE_3] in answers_yes.values()
        ):
            report: str = all_reports["report_yes_2_3"]
        elif (
            len(answers_yes) == 2
            and answer_yes_options[ANSWER_YES_CHOICE_1] in answers_yes.values()
            and answer_yes_options[ANSWER_YES_CHOICE_4] in answers_yes.values()
        ):
            report: str = all_reports["report_yes_1_4"]
        else:
            report: str = all_reports["report_yes_other"]

    return report


# # Define survey answers
# survey = Survey(Q1_answer='something' ... other answers )
#
# # Generate report based on survey answers
# report = Report(survey=survey)
# report.generate() # Outputs report text which is generated based on survey answers


def generate_report(
        q1_answer: str = None,
        q2_answer_1: str = None,
        q2_answer_2: str = None,
        q2_answer_3: str = None,
        q2_answer_4: str = None,
        q3_time_period: int = None,
        q3_unit_of_time: str = None,
        q4_answer_1: str = None,
        **q4_answers_yes: str

) -> str:
    report: str = ""

    q1_report: str = question_1(q1_answer)
    q2_report: str = question_2(
        q2_answer_1, q2_answer_2, q2_answer_3, q2_answer_4
    )
    q3_report: str = question_3(q3_time_period, q3_unit_of_time)
    q4_report: str = question_4(q4_answer_1, **q4_answers_yes)

    report_list: List[str] = [q1_report, q2_report, q3_report, q4_report]

    for report_part in report_list:
        report += f"{report_part}\n=====\n"

    return report


print(
    generate_report(
        q1_answer=a_1_1,
        q2_answer_1=a_2_1,
        q2_answer_3=a_2_3,
        q2_answer_4=a_2_4,
        q3_time_period=a_3_241_m,
        q3_unit_of_time=a_3_minutes,
        q4_answer_1=a_4_yes,
        q4_answer_yes_2=a_4_yes_2,
        q4_answer_yes_3=a_4_yes_3
    )
)
