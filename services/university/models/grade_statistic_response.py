from pydantic import BaseModel

from services.university.models.grade_base_model import Field


class GradeStatisticResponse(BaseModel):
    count: int
    min: int | None = Field(None, ge=0, le=5, description="Минимальная оценка")
    max: int | None = Field(None, ge=0, le=5, description="Максимальная оценка")
    avg: float | None = Field(None, ge=0.0, le=5.0, description="Средняя оценка")
