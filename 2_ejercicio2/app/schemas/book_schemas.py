from pydantic import BaseModel, Field, field_validator
from app.models.book_models import Category


class BookBase(BaseModel):
    title: str = Field(..., max_length=50)
    author: str = Field(..., max_length=30)
    isbn: str = Field(...)
    pages: int = Field(..., gt=0)
    category: Category = Field(...)
    available_copies: int = Field(..., ge=0)

    @field_validator("isbn")
    @classmethod
    def validate_isbn(cls, value):
        # if len(value) != 10 and len(value) != 13:
        if len(value) not in [10, 13]:
            raise ValueError("ISBN solo puede contener 10 o 13 digitos")
        return value


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int
