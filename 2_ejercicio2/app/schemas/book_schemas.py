from pydantic import BaseModel, Field
from app.services.book_services import Category


class BookBase(BaseModel):
    title: str = Field(..., max_length=50)
    author: str = Field(..., max_length=30)
    isbn: str = Field(...)
    pages: int = Field(..., gt=0)
    category: Category = Field(...)
    available_copies: int = Field(..., ge=0)
