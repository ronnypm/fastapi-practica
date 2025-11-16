from pydantic import BaseModel, Field, field_validator
from datetime import date


class TaskCreate(BaseModel):
    title: str = Field(..., max_length=30)
    description: str = Field(..., min_length=10, max_length=100)
    priority: int = Field(ge=1, le=5)
    due_date: date

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        cleaned = value.strip()
        if cleaned < 3:
            raise ValueError("Titulo muy corto")
        return cleaned

    @field_validator("description")
    @classmethod
    def validate_description(cls, value):
        cleaned = value.strip()
        if len(cleaned) < 10:
            raise ValueError(
                "La descripción debe tener al menos 10 caracteres (sin contar espacios)")
        if len(cleaned) > 100:
            raise ValueError(
                "La descripción no puede exceder 100 caracteres")
        return cleaned

    @field_validator("due_date")
    @classmethod
    def validator_due_date(cls, value):
        if value < date.today():
            raise ValueError(
                "La fecha de entrega no puede ser anterior a la actual")
        return value


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    due_date: date
    completed: bool


class TaskUpdatePriority(BaseModel):
    priority: int = Field(ge=1, le=5)
