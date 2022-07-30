from typing import Dict

ANSWER_1: int = 0
ANSWER_2: int = 1
ANSWER_3: int = 2
ANSWER_4: int = 3
ANSWER_5: int = 4

q1: str = "Which field are you working in?"


def question_1(answer: str) -> str:
    answer_options: Dict[int, str] = {
        ANSWER_1: "Customer Support",
        ANSWER_2: "Engineering and technical fields",
        ANSWER_3: "Pharmaceutical and biotechnology areas",
        ANSWER_4: "Scientific and academic fields",
        ANSWER_5: "Electronic discovery",

    }

    all_reports: Dict[str, str] = {
        "report_1": (
            "Lorem ipsum 1. Question - ANSWER_1 dolor sit amet, consectetur "
            "adipiscing elit. Mauris sed ligula vitae tellus pellentesque "
            "vehicula"
            " nec eu velit. Curabitur luctus et nibh et ornare. Suspendisse "
            "non "
            "mattis lacus. Cras vitae mi ornare, euismod velit sit amet, "
            "iaculis "
            "tortor. In tempor purus sapien.\n\nDonec tincidunt 1. Question -"
            " "
            "ANSWER_1 metus nec dui tristique malesuada. Praesent lectus nunc,"
            " "
            "accumsan vel justo in, imperdiet faucibus leo. Nullam efficitur"
            " massa"
            " nec turpis tincidunt, feugiat viverra erat rutrum. Aliquam eget"
            " "
            "auctor lectus, mollis blandit ipsum. Phasellus maximus finibus "
            "arcu "
            "a tincidunt."
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
            "Sed vel bibendum tortor. Proin a aliquet tortor. Vivamus rhoncus "
            "1. "
            "Question - ANSWER_3 risus nec ultricies rutrum. Mauris bibendum "
            "lectus risus, non porttitor urna interdum quis.\n\nSuspendisse "
            "quis "
            "risus scelerisque, 1. Question - ANSWER_3 feugiat augue nec, "
            "semper "
            "leo. Fusce euismod facilisis mi, tristique sollicitudin metus "
            "hendrerit non. Nulla ac sodales quam, sit amet finibus metus. Ut"
            " in "
            "felis tellus. Sed aliquet metus ullamcorper est vestibulum "
            "mattis. "
            "Cras nisi sem, euismod in egestas vel, ullamcorper ac sapien. In "
            "porttitor elementum faucibus."
        ),
        "report_4": (
            "Mauris urna nunc, eleifend id sapien eget, tincidunt venenatis "
            "risus."
            " Vestibulum imperdiet enim at nibh sodales, 1. Question - "
            "ANSWER_4 or"
            " ANSWER_5 or ANSWER_6 eget scelerisque odio finibus.\n\nNullam ut"
            " mi"
            " eget sapien accumsan iaculis. Vestibulum in maximus metus, "
            "1. Question - ANSWER_4 or ANSWER_5 or ANSWER_6 vitae venenatis "
            "sapien. Nullam auctor odio vehicula, posuere elit in, ullamcorper"
            " lectus. Mauris pharetra dapibus congue. Suspendisse potenti."
        ),
    }

    answer_reports: Dict[str, str] = {
        answer_options[ANSWER_1]: all_reports["report_1"],
        answer_options[ANSWER_2]: all_reports["report_2"],
        answer_options[ANSWER_3]: all_reports["report_3"],
        answer_options[ANSWER_4]: all_reports["report_4"],
        answer_options[ANSWER_5]: all_reports["report_4"],
    }

    return answer_reports[answer]


# print(f"report for answer_1:\n{question_1('Customer Support')}\n")
# print(
#     f"report for answer_2:\n{question_1('Engineering and technical fields')}\n"
# )
# print(
#     f"report for answer_3:\n"
#     f"{question_1('Pharmaceutical and biotechnology areas')}\n"
# )
# print(
#     f"report for answer_4:\n{question_1('Scientific and academic fields')}\n"
# )
# print(f"report for answer_5:\n{question_1('Electronic discovery')}")


# q2: str = ""
#
#
# def question_2(answer: str) -> str:
#     all_reports: Dict[str, str] = {}
#
#     reply_reports: Dict[str, str] = {}
#
#     return reply_reports[answer]


q3: str = ""


def question_3(*answers: str) -> str:
    answer_options: Dict[int, str] = {
        ANSWER_1: (
            "Creating, reading, updating and deleting entries in a database"
        ),
        ANSWER_2: "Computations",
        ANSWER_3: "Text-based data processing",
        ANSWER_4: "Retrieving data from third-party sources",
    }

    all_reports: Dict[str, str] = {
        "report_1": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed "
            "sollicitudin leo in 3. Question - ANSWER_4, ANSWER_3 and ANSWER_1"
            " lectus cursus tincidunt. Nullam dapibus tincidunt libero nec "
            "volutpat.\n\nCras sit amet massa a turpis malesuada ornare vitae "
            "sed arcu. Maecenas eleifend rutrum augue, eget imperdiet sem "
            "gravida sed. Vestibulum vel libero consectetur, 3. Question - "
            "ANSWER_4, ANSWER_3 and ANSWER_1 pellentesque lacus nec, facilisis"
            " nisl. Phasellus faucibus lobortis tincidunt. Duis tristique "
            "congue bibendum.\n\nMorbi semper cursus felis et consequat. Nulla"
            " posuere, quam eget pulvinar 3. Question - ANSWER_4, ANSWER_3 and"
            " ANSWER_1 dignissim, odio sem euismod leo, at ornare purus massa "
            "quis sapien. Aliquam eget libero nec lectus placerat congue. "
            "Aenean nec tortor a ligula aliquam pharetra. Aenean et magna "
            "enim."
        ),
        "report_2": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            " Vestibulum dictum, dui non auctor tristique, odio sem "
            "3. Question - ANSWER_2 and ANSWER_4 convallis lacus, non"
            " gravida libero erat id justo. Praesent in varius nisi."
            " Phasellus suscipit elit sit amet aliquam tincidunt."
            "\n\nIn pellentesque gravida risus, et 3. Question - "
            "ANSWER_2 and ANSWER_4 rhoncus quam. Vestibulum ac risus "
            "nulla. Phasellus iaculis interdum pulvinar. Vivamus sit "
            "amet sagittis risus. Morbi ut pellentesque sapien."
        ),
        "report_3": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras "
            "viverra luctus nunc, non ultrices mauris molestie vitae. Sed "
            "gravida purus finibus 3. Question - ANSWER_4, ANSWER_3 or "
            "ANSWER_1 efficitur congue. Vestibulum magna urna, volutpat vitae"
            " auctor non, pharetra vel leo.\n\nInterdum et malesuada fames ac"
            " ante ipsum primis in faucibus. Vestibulum elementum sagittis "
            "tortor, vel porta leo tristique ac. Phasellus ac metus est. 3. "
            "Question - ANSWER_4, ANSWER_3 or ANSWER_1 Aenean vel malesuada "
            "ex, nec rutrum justo. Sed ultricies venenatis mauris, in pharetra"
            " ante vulputate nec. Proin viverra convallis augue elementum "
            "volutpat."
        ),
        "report_4": (
            "Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
            "labore et dolore magna aliqua. Ut enim ad minim veniam, quis "
            "nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
            "commodo consequat.\n\nDuis aute irure dolor in reprehenderit in "
            "voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
            "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui"
            " officia deserunt mollit anim id est laborum."
        ),

    }

    if (
            len(answers) == 3
            and answer_options[ANSWER_1] in answers
            and answer_options[ANSWER_3] in answers
            and answer_options[ANSWER_4] in answers
    ):
        report = all_reports["report_1"]
    elif(
            len(answers) == 2
            and answer_options[ANSWER_2] in answers
            and answer_options[ANSWER_4] in answers
    ):
        report = all_reports["report_2"]
    elif(
            len(answers) == 1
            and (answer_options[ANSWER_1] in answers
            or answer_options[ANSWER_3] in answers
            or answer_options[ANSWER_4] in answers)
    ):
        report = all_reports["report_3"]
    else:
        report = all_reports["report_4"]

    return report


# a1 = "Creating, reading, updating and deleting entries in a database"
# a2 = "Computations"
# a3 = "Text-based data processing"
# a4 = "Retrieving data from third-party sources"
#
# print(
#     f"report if answers 1, 3 and 4 are chosen:\n"
#     f"{question_3(a1, a3, a4)}\n"
# )
# print(
#     f"report if answers 2 and 4 are chosen:\n"
#     f"{question_3(a2, a4)}\n"
# )
# print(
#     f"report if answer 1 is chosen:\n"
#     f"{question_3(a1)}\n"
# )
# print(
#     f"report if answer 3 is chosen:\n"
#     f"{question_3(a3)}\n"
# )
# print(
#     f"report if answer 4 is chosen:\n"
#     f"{question_3(a4)}\n"
# )
# print(
#     f"report for other combinations:\n"
#     f"{question_3(a2)}\n"
# )
