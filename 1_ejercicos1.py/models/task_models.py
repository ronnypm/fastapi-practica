from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    id: int
    title: str
    description: str
    priority: int
    due_date: date
    completed: bool = False
