from typing import List
from models.task_models import Task
from database.db import task_list
from schemas.task_schemas import TaskCreate, TaskUpdatePriority, TaskComplete


# Listar todas las tareas


def get_all_tasks() -> List[Task]:
    return task_list

# Buscar tarea por ID


def search_task_by_id(task_id: int):
    return next((task for task in task_list if task.id == task_id), None)

# Buscar tareas segun su estado


def filter_by_status(task_list: list[Task], completed: bool) -> List[Task]:
    return [task for task in task_list if task.completed == completed]


def create_task(data: TaskCreate) -> Task:
    new_id = task_list[-1].id + 1 if task_list else 1
    new_task = Task(
        id=new_id,
        title=data.title,
        description=data.description,
        completed=False,
        priority=data.priority,
        due_date=data.due_date
    )
    task_list.append(new_task)
    return new_task


def task_completed(task_id: int, task_complete: TaskComplete):
    task = next((task for task in task_list if task.id == task_id), None)
    if task is None:
        return None
    task.completed = task_complete.completed
    return task


def task_priority(task_id: int, task_update_priority: TaskUpdatePriority):
    task = next((task for task in task_list if task.id == task_id), None)
    if task is None:
        return None
    task.priority = task_update_priority.priority
    return task


"""
Esto es la mejor forma que la utilizare a futuro
"""
# my_tasks: dict[int, Task] = {t.id: t for t in task_list}
# def search_task_by_id(task_id: int):
#     return my_tasks.get(task_id)
