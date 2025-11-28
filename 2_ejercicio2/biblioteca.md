Ejercicio 2: Sistema de Biblioteca (Books API)

Entidades:

    Book: id, title, author, isbn, pages, available_copies, category

Endpoints:

    GET /books - Todos los libros

    GET /books/{id} - Un libro

    GET /books/filter/by-author?author=García - Por autor

    POST /books - Agregar libro

    PATCH /books/{id}/borrow - Prestar libro (resta copies)

    PATCH /books/{id}/return - Devolver libro (suma copies)

Validaciones:

    isbn: formato específico (10 o 13 dígitos)

    pages: mayor a 0

    available_copies: no puede ser negativo

    category: ["fiction", "non-fiction", "science", "history"]
