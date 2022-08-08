from typing import Dict


class Survey:

    def __init__(self, answers: Dict):
        self.FIELD_OF_STUDY = answers["FIELD_OF_STUDY"]
        self.REQUIRED_FUNCTIONALITY = answers["REQUIRED_FUNCTIONALITY"]
        self.TASK_PROCESSING_TIME = answers["TASK_PROCESSING_TIME"]
        self.DO_YOU_WORK_REMOTELY = answers["DO_YOU_WORK_REMOTELY"]

    def __str__(self) -> str:
        return (
            f"FIELD_OF_STUDY: {self.FIELD_OF_STUDY}\n"
            f"REQUIRED_FUNCTIONALITY: {self.REQUIRED_FUNCTIONALITY}\n"
            f"TASK_PROCESSING_TIME: {self.TASK_PROCESSING_TIME}\n"
            f"DO_YOU_WORK_REMOTELY: {self.DO_YOU_WORK_REMOTELY}\n"
        )
