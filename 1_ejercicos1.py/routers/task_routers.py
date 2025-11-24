from fastapi import APIRouter, HTTPException, status
from typing import List

from schemas.task_schemas import TaskCreate, TaskResponse, TaskComplete, TaskUpdatePriority
from models.task_models import Task
from database.db import task_list
from services.tasks_services import get_all_tasks, search_task_by_id, filter_by_status


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


def fetch_last_id():
    return task_list[-1].id if task_list else 0


@router.post("/",
             response_model=TaskResponse,
             status_code=status.HTTP_201_CREATED,
             summary="Creacion de una nueva tarea",
             description="Ingreso de datos para la creacion de una nueva tarea en el sistema.",
             responses={
                 201: {
                     "description": "Tarea creada exitosamente",
                     "model": TaskResponse
                 },
                 400: {
                     "description": "Datos inválidos enviados"
                 }
             }
             )
async def create_new_task(task_create: TaskCreate):
    new_id = fetch_last_id() + 1
    new_task = Task(
        id=new_id,
        title=task_create.title,
        description=task_create.description,
        completed=False,
        priority=task_create.priority,
        due_date=task_create.due_date
    )
    task_list.append(new_task)
    return new_task


@router.patch(
    "/{task_id}/completed",
    response_model=TaskResponse,
    summary="Actualizar estado de tareas",
    description="Actulaliza el estado de completado de una tarea"
)
async def mark_task_completed(task_id: int, task_complete: TaskComplete):
    task = next((task for task in task_list if task.id == task_id), None)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    task.completed = task_complete.completed
    return task


@router.patch(
    "/{task_id}/priority",
    response_model=TaskResponse,
    summary="Actualizar prioridad de tarea",
    description="Actulaliza el estado de prioridad de una tarea"
)
async def update_task_completed(task_id: int, task_update_priority: TaskUpdatePriority):
    task = next((task for task in task_list if task.id == task_id), None)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    task.priority = task_update_priority.priority
    return task
