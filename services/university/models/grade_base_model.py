from enum import Enum

from pydantic import BaseModel, ConfigDict


class GradeEnum(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class GradeBaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int
    student_id: int
    grade: GradeEnum
