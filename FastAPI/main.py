from fastapi import FastAPI
from routers import prueba, ejercicio_1

app = FastAPI()
# Router
app.include_router(prueba.router)
app.include_router(ejercicio_1.router)


@app.get("/url")
async def root():
    return "Mi pagina principla"
