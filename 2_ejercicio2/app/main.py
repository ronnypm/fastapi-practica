from fastapi import FastAPI
from app.routers import book_routers

app = FastAPI(
    title="API SEARCH BOOKS",
    version="1.0.0",
    description="Gestion De Libros API"
)

app.include_router(book_routers.router)


@app.get("/")
async def root():
    return {"message": "API Book"}
