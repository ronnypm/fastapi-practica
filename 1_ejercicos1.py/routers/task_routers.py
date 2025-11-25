from fastapi import APIRouter, HTTPException, status
from typing import List

from schemas.task_schemas import TaskCreate, TaskResponse, TaskComplete, TaskUpdatePriority
from models.task_models import Task
from database.db import task_list
from services.tasks_services import get_all_tasks, search_task_by_id, filter_by_status, create_task, task_completed, task_priority


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/",
            response_model=List[TaskResponse],
            status_code=status.HTTP_200_OK,
            summary="Listar todas las tareas",
            description="Devuelve una lista con todas las tareas que se registran en el sistema",
            )
async def get_tasks():
    return get_all_tasks()


@router.get("/{task_id}",
            response_model=TaskResponse,
            status_code=status.HTTP_200_OK,
            summary="Obtener una tarea por ID",
            description="Devuelve los detalles de una tarea especifica"
            )
async def get_task_id(task_id: int):
    task = search_task_by_id(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarea no encontrada"
        )
    return task


@router.get(
    "/filter/by-status",
    response_model=list[TaskResponse],
    summary="Filtrado por estado",
    description="Filtra las tarea segun si estan completadas o no",
)
async def filter_tasks_by_status(completed: bool):
    return filter_by_status(task_list, completed)


@router.post("/",
             response_model=TaskResponse,
             status_code=status.HTTP_201_CREATED,
             summary="Creacion de una nueva tarea",
             description="Ingreso de datos para la creacion de una nueva tarea en el sistema.",
             )
async def create_new_task(task_create: TaskCreate):
    return create_task(task_create)


@router.patch(
    "/{task_id}/completed",
    response_model=TaskResponse,
    summary="Actualizar estado de tareas",
    description="Actulaliza el estado de completado de una tarea"
)
async def mark_task_completed(task_id: int, task_complete: TaskComplete):
    task = task_completed(task_id, task_complete)
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    return task


@router.patch(
    "/{task_id}/priority",
    response_model=TaskResponse,
    summary="Actualizar prioridad de tarea",
    description="Actulaliza el estado de prioridad de una tarea"
)
async def update_task_priority(task_id: int, task_update_priority: TaskUpdatePriority):
    task = task_priority(task_id, task_update_priority)
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    return task
