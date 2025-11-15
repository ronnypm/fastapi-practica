from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int


app = FastAPI()
user_list = [User(id=1, name="kenyu", surname="Pisfil", age=35),
             User(id=2, name="Nico", surname="Pisfil", age=34),
             User(id=3, name="Mari", surname="Pisfil", age=36)]


@app.get("/users/", )  # referencia a usuarios
async def usersjs():
    return user_list

# peticion get por id(path)
# http://127.0.0.1:8000/users/1


@app.get("/user/{id}")
async def user_id(id: int):
    user = search_user(id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Usuario no encontraod")


# peticion get por query
# http://127.0.0.1:8000/usersquery/?id=2
@app.get("/userquery/")
async def user_id(id: int):
    user = search_user(id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Usuario no encontraod")


# Creacion de post

@app.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    user_list.append(user)
    return user


# uso de put(actualiza)
@app.put("/user/")
async def user(user: User):
    found = False
    for index, save_user in enumerate(user_list):
        if save_user.id == user.id:
            user_list[index] = user
            found = True

    if not found:
        return {"Error": "No se ha actualizado el usuario"}

    return user


@app.delete("/user/{id}")
async def user(user: User):
    found = False
    for index, save_user in enumerate(user_list):
        if save_user.id == user.id:
            del user_list[index]

    if not found:
        return {"Error": "No se ha encontrado el usuario"}


def search_user(id: int):
    return next(filter(lambda user: user.id == id, user_list), None)
