from typing import List
from models.task_models import Task
from database.db import task_list
from datetime import datetime

# Listar todas las tareas


def get_all_tasks() -> List[Task]:
    return task_list

# Buscar tarea por ID


def search_task_by_id(task_id: int):
    return next((task for task in task_list if task.id == task_id), None)

# Buscar tareas segun su estado


def filter_by_status(task_list: list[Task], completed: bool) -> List[Task]:
    return [task for task in task_list if task.completed == completed]


"""
Esto es la mejor forma que la utilizare a futuro
"""
# my_tasks: dict[int, Task] = {t.id: t for t in task_list}
# def search_task_by_id(task_id: int):
#     return my_tasks.get(task_id)
