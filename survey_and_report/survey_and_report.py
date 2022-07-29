from typing import Dict

q1: str = "Which field are you working in?"


def question_1(answer: str) -> str:
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

    reply_reports: Dict[str, str] = {
        "Customer Support": all_reports["report_1"],
        "Engineering and technical fields": all_reports["report_2"],
        "Pharmaceutical and biotechnology areas": all_reports["report_3"],
        "Scientific and academic fields": all_reports["report_4"],
        "Electronic discovery": all_reports["report_4"],
    }

    return reply_reports[answer]


# for key, item in q1_reports.items():
#     print(f"{key}: {item}\n")

# print(question_1("Customer Support"))
# print(question_1("Engineering and technical fields"))
# print(question_1("Pharmaceutical and biotechnology areas"))
# print(question_1("Scientific and academic fields"))
# print(question_1("Electronic discovery"))

q2: str = ""


def question_2(answer: str) -> str:
    all_reports: Dict[str, str] = {}

    reply_reports: Dict[str, str] = {}

    return reply_reports[answer]
