from pydantic import BaseModel, Field, field_validator
from datetime import date


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3)
    description: str = Field(..., min_length=1, max_length=50)
    priority: int = Field(ge=1, le=5)
    due_date: date

    @field_validator("due_date")
    @classmethod
    def validator_due_date(cls, value, info):
        if value < date.today():
            raise ValueError(
                "La fecha de entrega no puede ser anterior a la actual")
        return value
