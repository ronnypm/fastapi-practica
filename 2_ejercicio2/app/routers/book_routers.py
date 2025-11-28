from fastapi import APIRouter, HTTPException, status
from typing import List
from app.database.book_database import books
from app.schemas.book_schemas import BookResponse
from app.services.book_services import get_all_books, get_id_book, get_book_author


router = APIRouter(prefix="/books", tags=["books"])


@router.get("/",
            response_model=List[BookResponse],
            summary="Listar todos los libros",
            description="Devuelve una lista con todos los libros que se registran en el sistema"
            )
async def get_books():
    return get_all_books()


@router.get("/{book_id}",
            response_model=BookResponse,
            summary="Obtener un libro por id",
            description="Devuelve los detalles de un libro especifico"
            )
async def get_book_by_id(book_id: int):
    book = get_id_book(book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book no found"
        )
    return book


@router.get("/filter/by-author",
            response_model=list[BookResponse],
            summary="Filtrar libros por autor",
            description="Devuelve todos los libros que tiene un autor en el sistema"
            )
async def get_book_by_author(author: str):
    return get_book_author(author)
