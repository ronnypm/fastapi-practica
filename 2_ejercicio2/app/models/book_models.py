from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str
    isbn: str
    pages: int
    available_copies: int
    category: str
