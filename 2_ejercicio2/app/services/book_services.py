from typing import List
from app.models.book_models import Book
from app.database.book_database import books


def get_all_books() -> List[Book]:
    return books


def get_id_book(book_id: int):
    return next((book for book in books if book.id == book_id), None)


def get_book_author(author: str) -> List[Book]:
    return [book for book in books if author.lower() in book.author.lower()]
