from pydantic import ConfigDict

from services.university.models.grade_base_model import GradeBaseModel, Field


class GradeStatisticResponse(GradeBaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int = Field(ge=0, description="Количество оценок")
    min: int | None = Field(None, ge=0, le=5, description="Минимальная оценка")
    max: int | None = Field(None, ge=0, le=5, description="Максимальная оценка")
    avg: float | None = Field(None, ge=0.0, le=5.0, description="Средняя оценка")
