from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from typing import List

from schemas.task_schemas import TaskCreate, TaskResponse, TaskUpdatePriority
from models.task_models import Task
from database.db import task_list


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/",
            response_model=list[TaskResponse],
            status_code=status.HTTP_200_OK,
            summary="Listar todas las tareas",
            description="Devuelve una lista con todas las tareas que se registran en el sistema",
            )
async def get_tasks():
    return task_list


my_tasks: dict[int:Task] = {t.id: t for t in task_list}


def search_task_by_id(task_id: int):
    return my_tasks.get(task_id)


@router.get("/{task_id}",
            response_model=TaskResponse,
            status_code=status.HTTP_200_OK,
            summary="Obtener una tarea por ID",
            description="Devuelve los detalles de una tarea especifica",
            responses={
                404: {
                    "description": "Tarea no encontrada",
                    "content": {
                        "application/json": {
                            "example": {"detail": "Tarea no encontrada"}
                        }
                    }
                }
            }

            )
async def get_task_id(task_id: int):
    task = search_task_by_id(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarea no encontrada"
        )
    return task


def filter_by_status(task_list, completed: bool):
    return [task for task in task_list if task.completed == completed]


@router.get(
    "/filter/by-status",
    response_model=list[TaskResponse],
    summary="Filtrado por estado",
    description="Filtra las tarea segun si estan completadas o no"
)
async def filter_tasks_by_status(completed: bool):
    return filter_by_status(task_list, completed)
