import unittest

from typing import Dict

from survey_and_report.survey_and_report import Report as r
from survey_and_report.survey_and_report import Survey as s


class TestQ1Report(unittest.TestCase):

    def setUp(self):
        self.answer_options: Dict[int, str] = {
            r.ANSWER_1: "Customer Support",
            r.ANSWER_2: "Engineering and technical fields",
            r.ANSWER_3: "Pharmaceutical and biotechnology areas",
            r.ANSWER_4: "Scientific and academic fields",
            r.ANSWER_5: "Electronic discovery",
        }

        self.report_options: Dict[str, str] = {
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

    def test_q1_report_for_answer_1(self):
        survey = s(q1_answer=self.answer_options[r.ANSWER_1])

        expected_result: str = self.report_options["report_1"]
        actual_result: str = r(survey).q1_report()

        self.assertEqual(expected_result, actual_result)

    def test_q1_report_for_answer_2(self):
        survey = s(q1_answer=self.answer_options[r.ANSWER_2])

        expected_result: str = self.report_options["report_2"]
        actual_result: str = r(survey).q1_report()

        self.assertEqual(expected_result, actual_result)

    def test_q1_report_for_answer_3(self):
        survey = s(q1_answer=self.answer_options[r.ANSWER_3])

        expected_result: str = self.report_options["report_3"]
        actual_result: str = r(survey).q1_report()

        self.assertEqual(expected_result, actual_result)

    def test_q1_report_for_answer_4(self):
        survey = s(q1_answer=self.answer_options[r.ANSWER_4])

        expected_result: str = self.report_options["report_4"]
        actual_result: str = r(survey).q1_report()

        self.assertEqual(expected_result, actual_result)

    def test_q1_report_for_answer_5(self):
        survey = s(q1_answer=self.answer_options[r.ANSWER_5])

        expected_result: str = self.report_options["report_4"]
        actual_result: str = r(survey).q1_report()

        self.assertEqual(expected_result, actual_result)


class TestQ2Report(unittest.TestCase):

    def setUp(self):
        self.answer_options: Dict[int, str] = {
            r.ANSWER_1: (
                "Creating, reading, updating and deleting database entries"
            ),
            r.ANSWER_2: "Computations",
            r.ANSWER_3: "Text-based data processing",
            r.ANSWER_4: "Retrieving data from third-party sources",
        }

        self.report_options: Dict[str, str] = {
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

    def test_q2_report_for_answers_1_3_and_4(self):
        survey = s(
            q2_answer_1=self.answer_options[r.ANSWER_1],
            q2_answer_3=self.answer_options[r.ANSWER_3],
            q2_answer_4=self.answer_options[r.ANSWER_4]
        )

        expected_result: str = self.report_options["report_1"]
        actual_result: str = r(survey).q2_report()

        self.assertEqual(expected_result, actual_result)

    def test_q2_report_for_answers_2_and_4(self):
        survey = s(
            q2_answer_2=self.answer_options[r.ANSWER_2],
            q2_answer_4=self.answer_options[r.ANSWER_4]
        )

        expected_result: str = self.report_options["report_2"]
        actual_result: str = r(survey).q2_report()

        self.assertEqual(expected_result, actual_result)

    def test_q2_report_for_answer_1(self):
        survey = s(q2_answer_1=self.answer_options[r.ANSWER_1])

        expected_result: str = self.report_options["report_3"]
        actual_result: str = r(survey).q2_report()

        self.assertEqual(expected_result, actual_result)

    def test_q2_report_for_answer_3(self):
        survey = s(q2_answer_3=self.answer_options[r.ANSWER_3])

        expected_result: str = self.report_options["report_3"]
        actual_result: str = r(survey).q2_report()

        self.assertEqual(expected_result, actual_result)

    def test_q2_report_for_answer_4(self):
        survey = s(q2_answer_4=self.answer_options[r.ANSWER_4])

        expected_result: str = self.report_options["report_3"]
        actual_result: str = r(survey).q2_report()

        self.assertEqual(expected_result, actual_result)

    def test_q2_report_for_any_other_combination(self):
        survey = s(q2_answer_2=self.answer_options[r.ANSWER_2])

        expected_result: str = self.report_options["report_4"]
        actual_result: str = r(survey).q2_report()

        self.assertEqual(expected_result, actual_result)


class TestQ3Report(unittest.TestCase):

    def setUp(self):
        self.report_options: Dict[str, Dict[str, str]] = {
            "minutes": {
                "report_241": (
                    f"Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    f" Recommended shift duration: "
                    f"{round(241 * 1.5, 1)} minutes Vivamus hendrerit arcu "
                    f"eros, nec bibendum mi sodales id. Ut auctor nisl a "
                    f"placerat porttitor. Duis at tortor posuere, gravida "
                    f"sapien in, fermentum ligula.\n\nQuisque eu ipsum "
                    f"lobortis, hendrerit justo vitae, varius nisi. Etiam in "
                    f"leo feugiat purus facilisis tempor. Fusce congue metus "
                    f"non massa mollis, id imperdiet ex viverra. Cras "
                    f"Recommended shift duration: {round(241 * 1.5, 1)} "
                    f"minutes imperdiet lectus at imperdiet ornare."
                ),
                "report_119": (
                    f"Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    f" Integer porta at odio ac rhoncus. Recommended shift "
                    f"duration: {round(119 * 1.5 * 3.5, 1)} minutes Integer "
                    f"viverra porta eros nec ultrices. Nullam ante sem, "
                    f"tincidunt vitae orci id, vestibulum auctor risus. "
                    f"Phasellus sit amet lobortis eros. Maecenas convallis "
                    f"dolor ex, vel congue ipsum ornare eu.\n\nNunc in mattis "
                    f"dolor, quis posuere lorem. Recommended shift duration: "
                    f"{round(119 * 1.5 * 3.5, 1)} minutes Nullam condimentum "
                    f"semper diam, lacinia tempor eros tristique ut. Etiam "
                    f"ultrices imperdiet tortor at eleifend. Aenean lorem "
                    f"felis, volutpat eu euismod at, congue id erat. Duis "
                    f"luctus quam vitae mattis tempus."
                ),
                "report_200": (
                    f"Sed at aliquam ex. Vestibulum maximus erat in justo "
                    f"maximus posuere. Recommended shift duration: "
                    f"{round(200 * 1.5 * 2.67, 1)} minutes Suspendisse tellus "
                    f"magna, faucibus scelerisque dapibus et, luctus egestas "
                    f"nibh. Pellentesque eleifend mauris ac volutpat "
                    f"ullamcorper.\n\nAenean vitae velit et nulla egestas "
                    f"viverra sit amet eu eros. Recommended shift duration: "
                    f"{round(200 * 1.5 * 2.67, 1)} minutes Nunc congue rutrum "
                    f"sem"
                ),
            },
            "hours": {
                "report_5": (
                    f"Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    f" Recommended shift duration: "
                    f"{round(5 * 1.5, 1)} hours Vivamus hendrerit arcu "
                    f"eros, nec bibendum mi sodales id. Ut auctor nisl a "
                    f"placerat porttitor. Duis at tortor posuere, gravida "
                    f"sapien in, fermentum ligula.\n\nQuisque eu ipsum "
                    f"lobortis, hendrerit justo vitae, varius nisi. Etiam in "
                    f"leo feugiat purus facilisis tempor. Fusce congue metus "
                    f"non massa mollis, id imperdiet ex viverra. Cras "
                    f"Recommended shift duration: {round(5 * 1.5, 1)} "
                    f"hours imperdiet lectus at imperdiet ornare."
                ),
                "report_1": (
                    f"Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    f" Integer porta at odio ac rhoncus. Recommended shift "
                    f"duration: {round(1 * 1.5 * 3.5, 1)} hours Integer "
                    f"viverra porta eros nec ultrices. Nullam ante sem, "
                    f"tincidunt vitae orci id, vestibulum auctor risus. "
                    f"Phasellus sit amet lobortis eros. Maecenas convallis "
                    f"dolor ex, vel congue ipsum ornare eu.\n\nNunc in mattis "
                    f"dolor, quis posuere lorem. Recommended shift duration: "
                    f"{round(1 * 1.5 * 3.5, 1)} hours Nullam condimentum "
                    f"semper diam, lacinia tempor eros tristique ut. Etiam "
                    f"ultrices imperdiet tortor at eleifend. Aenean lorem "
                    f"felis, volutpat eu euismod at, congue id erat. Duis "
                    f"luctus quam vitae mattis tempus."
                ),
                "report_3": (
                    f"Sed at aliquam ex. Vestibulum maximus erat in justo "
                    f"maximus posuere. Recommended shift duration: "
                    f"{round(3 * 1.5 * 2.67, 1)} hours Suspendisse tellus "
                    f"magna, faucibus scelerisque dapibus et, luctus egestas "
                    f"nibh. Pellentesque eleifend mauris ac volutpat "
                    f"ullamcorper.\n\nAenean vitae velit et nulla egestas "
                    f"viverra sit amet eu eros. Recommended shift duration: "
                    f"{round(3 * 1.5 * 2.67, 1)} hours Nunc congue rutrum "
                    f"sem"
                ),
            },
        }



    def test_q3_report_if_time_period_more_than_240_minutes(self):
        survey = s(
            q3_time_period=241,
            q3_unit_of_time="minutes"
        )

        expected_result: str = self.report_options["minutes"]["report_241"]
        actual_result: str = r(survey).q3_report()

        self.assertEqual(expected_result, actual_result)

    def test_q3_report_if_time_period_more_than_4_hours(self):
        survey = s(
            q3_time_period=5,
            q3_unit_of_time="hours"
        )

        expected_result: str = self.report_options["hours"]["report_5"]
        actual_result: str = r(survey).q3_report()

        self.assertEqual(expected_result, actual_result)

    def test_q3_report_if_time_period_less_than_120_minutes(self):
        survey = s(
            q3_time_period=119,
            q3_unit_of_time="minutes"
        )

        expected_result: str = self.report_options["minutes"]["report_119"]
        actual_result: str = r(survey).q3_report()

        self.assertEqual(expected_result, actual_result)

    def test_q3_report_if_time_period_less_than_2_hours(self):
            survey = s(
                q3_time_period=1,
                q3_unit_of_time="hours"
            )

            expected_result: str = self.report_options["hours"]["report_1"]
            actual_result: str = r(survey).q3_report()

            self.assertEqual(expected_result, actual_result)

    def test_q3_report_in_any_other_case_if_minutes_are_chosen(self):
        survey = s(
            q3_time_period=200,
            q3_unit_of_time="minutes"
        )

        expected_result: str = self.report_options["minutes"]["report_200"]
        actual_result: str = r(survey).q3_report()

        self.assertEqual(expected_result, actual_result)

    def test_q3_report_in_any_other_case_if_hours_are_chosen(self):
        survey = s(
            q3_time_period=3,
            q3_unit_of_time="hours"
        )

        expected_result: str = self.report_options["hours"]["report_3"]
        actual_result: str = r(survey).q3_report()

        self.assertEqual(expected_result, actual_result)


class TestQ4Report(unittest.TestCase):

    def setUp(self):
        self.answer_1_options: Dict[int, str] = {
            r.ANSWER_YES: "Yes",
            r.ANSWER_NO: "No",
            r.ANSWER_I_DONT_KNOW: "I don't know",
        }

        self.answer_yes_options: Dict[int, str] = {
            r.ANSWER_YES_CHOICE_1: (
                "Gathering and processing data, "
                "developing solutions by yourself"
            ),
            r.ANSWER_YES_CHOICE_2: "Email correspondence",
            r.ANSWER_YES_CHOICE_3: "Live chat correspondence",
            r.ANSWER_YES_CHOICE_4: "Phone calls",
        }

        self.report_options: Dict[str, str] = {
            "report_dont_know": "Phasellus ac sem ornare, ANSWER_I_DONT_KNOW "
                                "euismod tellus id, sagittis felis. Nullam "
                                "viverra est nibh, et dignissim elit tincidunt"
                                " nec. Integer vel dolor aliquam, eleifend "
                                "metus in, tincidunt erat. Nam id facilisis "
                                "tortor.\n\nDonec malesuada, libero nec "
                                "tincidunt ANSWER_I_DONT_KNOW commodo, nulla "
                                "velit imperdiet mauris, sit amet cursus dui "
                                "quam maximus justo. In accumsan nisi ut orci "
                                "finibus ullamcorper. Aliquam consequat risus "
                                "non orci dapibus, id commodo erat egestas.",
            "report_no": "Nam maximus et massa laoreet congue. In facilisis "
                         "egestas neque. Nullam ac euismod nibh. ANSWER_NO "
                         "Aenean pulvinar lacinia ligula, nec lobortis magna "
                         "accumsan sed.\n\nDuis tempor pellentesque quam. "
                         "ANSWER_NO Sed non est dui. Sed commodo odio vel "
                         "augue pellentesque, et sagittis dolor tristique. "
                         "Phasellus mollis magna eu egestas viverra. Cras "
                         "elementum erat vel libero venenatis, ut suscipit "
                         "nibh scelerisque.",
            "report_yes_2_3": "Mauris viverra lobortis ante, eget faucibus "
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
                              "odio.",
            "report_yes_1_4": "Fusce sem est, maximus ac efficitur in, "
                              "accumsan eu libero. Praesent facilisis, augue "
                              "at pretium malesuada, ANSWER_YES and "
                              "ANSWER_YES_CHOICE_1, ANSWER_YES_CHOICE_4 erat "
                              "eros eleifend velit, at iaculis nunc nisi nec "
                              "odio. Ut consequat ac metus a bibendum. Donec "
                              "venenatis euismod eros ac dignissim. Donec "
                              "dictum odio a augue tincidunt interdum.",
            "report_yes_other": "Lorem ipsum dolor sit amet, consectetur "
                                "adipiscing elit. Pellentesque sed scelerisque"
                                " nulla, at mattis mauris. Vestibulum "
                                "dignissim viverra nulla quis tempus. "
                                "(Any other case)\nDonec finibus nisl sapien, "
                                "sed auctor elit sodales ac. Nulla dictum ante"
                                " ante, eget maximus mi efficitur nec.",
        }

    def test_q4_report_if_dont_know_is_chosen(self):
        survey = s(
            q4_yes_no_answer=self.answer_1_options[r.ANSWER_I_DONT_KNOW]
        )

        expected_result: str = self.report_options["report_dont_know"]
        actual_result: str = r(survey).q4_report()

        self.assertEqual(expected_result, actual_result)

    def test_q4_report_if_no_is_chosen(self):
        survey = s(
            q4_yes_no_answer=self.answer_1_options[r.ANSWER_NO]
        )

        expected_result: str = self.report_options["report_no"]
        actual_result: str = r(survey).q4_report()

        self.assertEqual(expected_result, actual_result)

    def test_q4_report_if_yes_and_options_2_and_3_are_chosen(self):
        survey = s(
            q4_yes_no_answer=self.answer_1_options[r.ANSWER_YES],
            q4_yes_option_2=self.answer_yes_options[r.ANSWER_YES_CHOICE_2],
            q4_yes_option_3=self.answer_yes_options[r.ANSWER_YES_CHOICE_3]
        )

        expected_result: str = self.report_options["report_yes_2_3"]
        actual_result: str = r(survey).q4_report()

        self.assertEqual(expected_result, actual_result)

    def test_q4_report_if_yes_and_options_1_and_4_are_chosen(self):
        survey = s(
            q4_yes_no_answer=self.answer_1_options[r.ANSWER_YES],
            q4_yes_option_1=self.answer_yes_options[r.ANSWER_YES_CHOICE_1],
            q4_yes_option_4=self.answer_yes_options[r.ANSWER_YES_CHOICE_4]
        )

        expected_result: str = self.report_options["report_yes_1_4"]
        actual_result: str = r(survey).q4_report()

        self.assertEqual(expected_result, actual_result)

    def test_q4_report_if_any_other_combination_is_chosen(self):
        survey = s(
            q4_yes_no_answer=self.answer_1_options[r.ANSWER_YES],
            q4_yes_option_2=self.answer_yes_options[r.ANSWER_YES_CHOICE_2]
        )

        expected_result: str = self.report_options["report_yes_other"]
        actual_result: str = r(survey).q4_report()

        self.assertEqual(expected_result, actual_result)


class TestOverallReport(unittest.TestCase):

    def test_overall_report_generation(self):
        q1_answer: str = "Customer Support"
        q2_answer_1: str = (
            "Creating, reading, updating and deleting database entries"
        )
        q2_answer_3: str = "Text-based data processing"
        q2_answer_4: str = "Retrieving data from third-party sources"
        q3_time_period: int = 241
        q3_unit_of_time: str = "minutes"
        q4_yes_no_answer: str = "I don't know"

        survey = s(
            q1_answer=q1_answer,
            q2_answer_1=q2_answer_1,
            q2_answer_3=q2_answer_3,
            q2_answer_4=q2_answer_4,
            q3_time_period=q3_time_period,
            q3_unit_of_time=q3_unit_of_time,
            q4_yes_no_answer=q4_yes_no_answer
        )

        report_parts: Dict[str, str] = {
            "q1_report": (
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
            "q2_report": (
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
            "q3_report": (
                    f"Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    f" Recommended shift duration: "
                    f"{round(241 * 1.5, 1)} minutes Vivamus hendrerit arcu "
                    f"eros, nec bibendum mi sodales id. Ut auctor nisl a "
                    f"placerat porttitor. Duis at tortor posuere, gravida "
                    f"sapien in, fermentum ligula.\n\nQuisque eu ipsum "
                    f"lobortis, hendrerit justo vitae, varius nisi. Etiam in "
                    f"leo feugiat purus facilisis tempor. Fusce congue metus "
                    f"non massa mollis, id imperdiet ex viverra. Cras "
                    f"Recommended shift duration: {round(241 * 1.5, 1)} "
                    f"minutes imperdiet lectus at imperdiet ornare."
                ),
            "q4_report": (
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
        }

        expected_result: str = (
            f"{report_parts['q1_report']}\n\n{report_parts['q2_report']}\n\n"
            f"{report_parts['q3_report']}\n\n{report_parts['q4_report']}\n\n"
        )
        actual_result: str = r(survey).generate()

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
