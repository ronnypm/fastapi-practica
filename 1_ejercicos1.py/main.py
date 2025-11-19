from fastapi import FastAPI
from routers import task_routers

app = FastAPI(
    title="TO DO API",
    version="1.0.0",
    description="API para gestionar tareas",
)
app.include_router(task_routers.router)


@app.get("/")
async def root():
    return {"message": "TO-DO API"}
