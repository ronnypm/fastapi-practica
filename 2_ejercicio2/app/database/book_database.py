from app.models.book_models import Book
books = [
    Book(
        id=1,
        title="Clean Code",
        author="Robert C. Martin",
        isbn="9780132350884",
        pages=464,
        category="science",
        available_copies=5
    ),
    Book(
        id=2,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        isbn="0261102214",
        pages=310,
        category="fiction",
        available_copies=10
    ),
    Book(
        id=3,
        title="Sapiens",
        author="Yuval Noah Harari",
        isbn="9780062316097",
        pages=443,
        category="history",
        available_copies=0
    ),
    Book(
        id=4,
        title="La Metamorfosis",
        author="Kafka",
        isbn="9780062316123",
        pages=99,
        category="fiction",
        available_copies=8
    ),
    Book(
        id=5,
        title="Cartas a mi Padre",
        author="Kafka",
        isbn="9780062316129",
        pages=120,
        category="fiction",
        available_copies=1
    )
]
