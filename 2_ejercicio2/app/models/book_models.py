from dataclasses import dataclass
from enum import Enum


@dataclass
class Book:
    id: int
    title: str
    author: str
    isbn: str
    pages: int
    available_copies: int
    category: str


class Category(Enum):
    FICTION = "fiction"
    NON_FICTION = "non-fiction"
    SCIENCE = "science"
    HISTORY = "history"
