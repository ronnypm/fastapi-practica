from fastapi import APIRouter

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"message": "No encontrado"}})

product_list = ["Pedro 1", "Juan 2", "Antonio 3"]


@router.get("/")
async def product():
    return product_list


@router.get("/{id}")
async def product(id: int):
    return product_list[id]
