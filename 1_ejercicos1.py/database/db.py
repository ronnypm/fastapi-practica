from datetime import date
from models.task_models import Task

task_list = [
    Task(
        id=1,
        title="Preparar informe mensual",
        description="Redactar el informe de ventas del mes",
        completed=False,
        priority=2,
        due_date=date(2025, 3, 10)
    ),
    Task(
        id=2,
        title="Revisar correos pendientes",
        description="Responder correos de clientes acumulados",
        completed=False,
        priority=3,
        due_date=date(2025, 3, 5)
    ),
    Task(
        id=3,
        title="Actualizar sistema",
        description="Instalar actualizaciones del servidor",
        completed=False,
        priority=1,
        due_date=date(2025, 2, 28)
    ),
    Task(
        id=4,
        title="Planificar sprint",
        description="Organizar tareas para el próximo sprint",
        completed=False,
        priority=1,
        due_date=date(2025, 3, 8)
    ),
    Task(
        id=5,
        title="Hacer backup general",
        description="Hacer un backup de todo el sistema",
        completed=False,
        priority=2,
        due_date=date(2025, 3, 15)
    )
]
