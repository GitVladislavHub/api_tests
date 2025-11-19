from pydantic import BaseModel

from services.university.models.grade_base_model import Field, GRADE_MIN, GRADE_MAX


class GradeStatisticResponse(BaseModel):
    count: int
    min: int | None = Field(None, ge=GRADE_MIN, le=GRADE_MAX, description="Минимальная оценка")
    max: int | None = Field(None, ge=GRADE_MIN, le=GRADE_MAX, description="Максимальная оценка")
    avg: float | None = Field(None, ge=GRADE_MIN, le=GRADE_MAX, description="Средняя оценка")
