from typing import Dict, List

from survey import Survey


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


class Report(AnswerType):

    def __init__(self, survey: Survey):
        self.survey = survey

    def q1_report(self) -> str:
        answer_options: Dict[int, str] = {
            self.ANSWER_1: "Customer Support",
            self.ANSWER_2: "Engineering and technical fields",
            self.ANSWER_3: "Pharmaceutical and biotechnology areas",
            self.ANSWER_4: "Scientific and academic fields",
            self.ANSWER_5: "Electronic discovery",
        }

        report_options: Dict[str, str] = {
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
        }

        answer_reports: Dict[str, str] = {
            answer_options[self.ANSWER_1]: report_options["report_1"],
            answer_options[self.ANSWER_2]: report_options["report_2"],
            answer_options[self.ANSWER_3]: report_options["report_3"],
            answer_options[self.ANSWER_4]: report_options["report_4"],
            answer_options[self.ANSWER_5]: report_options["report_4"],
        }

        return answer_reports[self.survey.q1_answer]

    def q2_report(self) -> str:
        answer_options: Dict[int, str] = {
            self.ANSWER_1: (
                "Creating, reading, updating and deleting database entries"
            ),
            self.ANSWER_2: "Computations",
            self.ANSWER_3: "Text-based data processing",
            self.ANSWER_4: "Retrieving data from third-party sources",
        }

        report_options: Dict[str, str] = {
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
        }

        if (
                not self.survey.q2_answer_2
                and self.survey.q2_answer_1 == answer_options[self.ANSWER_1]
                and self.survey.q2_answer_3 == answer_options[self.ANSWER_3]
                and self.survey.q2_answer_4 == answer_options[self.ANSWER_4]
        ):
            report: str = report_options["report_1"]
        elif (
                not any([self.survey.q2_answer_1, self.survey.q2_answer_3])
                and self.survey.q2_answer_2 == answer_options[self.ANSWER_2]
                and self.survey.q2_answer_4 == answer_options[self.ANSWER_4]
        ):
            report: str = report_options["report_2"]
        elif (
                not self.survey.q2_answer_2
                and (
                        (
                            self.survey.q2_answer_1
                            == answer_options[self.ANSWER_1]
                            and not any([
                                self.survey.q2_answer_3,
                                self.survey.q2_answer_4
                            ])
                        )
                        or (
                                (
                                    self.survey.q2_answer_3
                                    == answer_options[self.ANSWER_3]
                                    and not any([
                                        self.survey.q2_answer_1,
                                        self.survey.q2_answer_4
                                    ])
                                )
                        )
                        or (
                                (
                                    self.survey.q2_answer_4
                                    == answer_options[self.ANSWER_4]
                                    and not any([
                                        self.survey.q2_answer_1,
                                        self.survey.q2_answer_3
                                    ])
                                )
                        )
                )
        ):
            report: str = report_options["report_3"]
        else:
            report: str = report_options["report_4"]

        return report

    def q3_report(self) -> str:
        report_options: Dict[str, str] = {
            "report_1": (
                f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                f"Recommended shift duration: "
                f"{round(self.survey.q3_time_period * 1.5, 1)} "
                f"{self.survey.q3_unit_of_time} Vivamus hendrerit arcu eros, "
                f"nec bibendum mi sodales id. Ut auctor nisl a placerat "
                f"porttitor. Duis at tortor posuere, gravida sapien in, "
                f"fermentum ligula.\n\nQuisque eu ipsum lobortis, hendrerit "
                f"justo vitae, varius nisi. Etiam in leo feugiat purus "
                f"facilisis tempor. Fusce congue metus non massa mollis, id "
                f"imperdiet ex viverra. Cras Recommended shift duration: "
                f"{round(self.survey.q3_time_period * 1.5, 1)} "
                f"{self.survey.q3_unit_of_time} imperdiet lectus at imperdiet "
                f"ornare."
            ),
            "report_2": (
                f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                f"Integer porta at odio ac rhoncus. Recommended shift "
                f"duration: {round(self.survey.q3_time_period * 1.5 * 3.5, 1)}"
                f" {self.survey.q3_unit_of_time} Integer viverra porta eros "
                f"nec ultrices. Nullam ante sem, tincidunt vitae orci id, "
                f"vestibulum auctor risus. Phasellus sit amet lobortis eros. "
                f"Maecenas convallis dolor ex, vel congue ipsum ornare eu.\n\n"
                f"Nunc in mattis dolor, quis posuere lorem. Recommended shift "
                f"duration: {round(self.survey.q3_time_period * 1.5 * 3.5, 1)}"
                f" {self.survey.q3_unit_of_time} Nullam condimentum semper "
                f"diam, lacinia tempor eros tristique ut. Etiam ultrices "
                f"imperdiet tortor at eleifend. Aenean lorem felis, volutpat "
                f"eu euismod at, congue id erat. Duis luctus quam vitae mattis"
                f" tempus."
            ),
            "report_3": (
                f"Sed at aliquam ex. Vestibulum maximus erat in justo maximus "
                f"posuere. Recommended shift duration: "
                f"{round(self.survey.q3_time_period * 1.5 * 2.67, 1)} "
                f"{self.survey.q3_unit_of_time} Suspendisse tellus magna, "
                f"faucibus scelerisque dapibus et, luctus egestas nibh. "
                f"Pellentesque eleifend mauris ac volutpat ullamcorper.\n\n"
                f"Aenean vitae velit et nulla egestas viverra sit amet eu "
                f"eros. Recommended shift duration: "
                f"{round(self.survey.q3_time_period * 1.5 * 2.67, 1)} "
                f"{self.survey.q3_unit_of_time} Nunc congue rutrum sem"
            ),
        }

        if (
                (
                        self.survey.q3_time_period > 240
                        and self.survey.q3_unit_of_time == "minutes"
                )
                or (
                self.survey.q3_time_period > 4
                and self.survey.q3_unit_of_time == "hours"
                )
        ):
            report: str = report_options["report_1"]
        elif (
                (
                        self.survey.q3_time_period < 120
                        and self.survey.q3_unit_of_time == "minutes"
                )
                or (
                        self.survey.q3_time_period < 2
                        and self.survey.q3_unit_of_time == "hours"
                )
        ):
            report: str = report_options["report_2"]
        else:
            report: str = report_options["report_3"]

        return report

    def q4_report(self) -> str:
        answer_1_options: Dict[int, str] = {
            self.ANSWER_YES: "Yes",
            self.ANSWER_NO: "No",
            self.ANSWER_I_DONT_KNOW: "I don't know",
        }

        answer_yes_options: Dict[int, str] = {
            self.ANSWER_YES_CHOICE_1: (
                "Gathering and processing data, "
                "developing solutions by yourself"
            ),
            self.ANSWER_YES_CHOICE_2: "Email correspondence",
            self.ANSWER_YES_CHOICE_3: "Live chat correspondence",
            self.ANSWER_YES_CHOICE_4: "Phone calls",
        }

        report_options: Dict[str, str] = {
            "report_dont_know": (
                "Phasellus ac sem ornare, ANSWER_I_DONT_KNOW "
                "euismod tellus id, sagittis felis. Nullam "
                "viverra est nibh, et dignissim elit tincidunt"
                " nec. Integer vel dolor aliquam, eleifend "
                "metus in, tincidunt erat. Nam id facilisis "
                "tortor.\n\nDonec malesuada, libero nec "
                "tincidunt ANSWER_I_DONT_KNOW commodo, nulla "
                "velit imperdiet mauris, sit amet cursus dui "
                "quam maximus justo. In accumsan nisi ut orci "
                "finibus ullamcorper. Aliquam consequat risus "
                "non orci dapibus, id commodo erat egestas."
            ),
            "report_no": (
                "Nam maximus et massa laoreet congue. In facilisis "
                "egestas neque. Nullam ac euismod nibh. ANSWER_NO "
                "Aenean pulvinar lacinia ligula, nec lobortis magna "
                "accumsan sed.\n\nDuis tempor pellentesque quam. "
                "ANSWER_NO Sed non est dui. Sed commodo odio vel "
                "augue pellentesque, et sagittis dolor tristique. "
                "Phasellus mollis magna eu egestas viverra. Cras "
                "elementum erat vel libero venenatis, ut suscipit "
                "nibh scelerisque."
            ),
            "report_yes_2_3": (
                "Mauris viverra lobortis ante, eget faucibus "
                "felis pulvinar et. Suspendisse urna diam, "
                "ANSWER_YES and ANSWER_YES_CHOICE_2, "
                "ANSWER_YES_CHOICE_3 elementum nec tincidunt "
                "ornare, convallis condimentum nisi.\n\nNam "
                "gravida ac magna eget cursus. ANSWER_YES and "
                "ANSWER_YES_CHOICE_2, ANSWER_YES_CHOICE_3 "
                "Maecenas fermentum lacus eu tempor condimentum."
                " Quisque tristique viverra justo, et mollis "
                "magna ornare a. In lacus elit, vestibulum a ex "
                "facilisis, faucibus gravida dui. Morbi "
                "consectetur egestas tempor. Sed neque ex, "
                "condimentum congue facilisis non, aliquet sed "
                "odio."
            ),
            "report_yes_1_4": (
                "Fusce sem est, maximus ac efficitur in, "
                "accumsan eu libero. Praesent facilisis, augue "
                "at pretium malesuada, ANSWER_YES and "
                "ANSWER_YES_CHOICE_1, ANSWER_YES_CHOICE_4 erat "
                "eros eleifend velit, at iaculis nunc nisi nec "
                "odio. Ut consequat ac metus a bibendum. Donec "
                "venenatis euismod eros ac dignissim. Donec "
                "dictum odio a augue tincidunt interdum."
            ),
            "report_yes_other": (
                "Lorem ipsum dolor sit amet, consectetur "
                "adipiscing elit. Pellentesque sed scelerisque"
                " nulla, at mattis mauris. Vestibulum "
                "dignissim viverra nulla quis tempus. "
                "(Any other case)\nDonec finibus nisl sapien, "
                "sed auctor elit sodales ac. Nulla dictum ante"
                " ante, eget maximus mi efficitur nec."
            ),
        }

        if (
                self.survey.q4_yes_no_answer
                == answer_1_options[self.ANSWER_I_DONT_KNOW]
        ):
            report: str = report_options["report_dont_know"]
        elif self.survey.q4_yes_no_answer == answer_1_options[self.ANSWER_NO]:
            report: str = report_options["report_no"]
        else:
            if (
                not any(
                    [self.survey.q4_yes_option_1, self.survey.q4_yes_option_4]
                )
                and (
                    self.survey.q4_yes_option_2
                    == answer_yes_options[self.ANSWER_YES_CHOICE_2]
                )
                and (
                    self.survey.q4_yes_option_3
                    == answer_yes_options[self.ANSWER_YES_CHOICE_3]
                )
            ):
                report: str = report_options["report_yes_2_3"]
            elif (
                not any(
                    [self.survey.q4_yes_option_2, self.survey.q4_yes_option_3]
                )
                and (
                    self.survey.q4_yes_option_1
                    == answer_yes_options[self.ANSWER_YES_CHOICE_1]
                )
                and (
                    self.survey.q4_yes_option_4
                    == answer_yes_options[self.ANSWER_YES_CHOICE_4]
                )
            ):
                report: str = report_options["report_yes_1_4"]
            else:
                report: str = report_options["report_yes_other"]

        return report

    def generate(self) -> str:
        report: str = ""

        q1_report: str = self.q1_report()
        q2_report: str = self.q2_report()
        q3_report: str = self.q3_report()
        q4_report: str = self.q4_report()

        report_list: List[str] = [q1_report, q2_report, q3_report, q4_report]

        for report_part in report_list:
            report += f"{report_part}\n\n"

        return report
