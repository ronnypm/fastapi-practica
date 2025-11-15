Ejercicio 1: Sistema de Tareas (To-Do API)

Entidades:

    Task: id, title, description, completed, priority (1-5), due_date

Endpoints:

    GET /tasks - Listar todas

    GET /tasks/{id} - Una tarea

    GET /tasks/filter/by-status?completed=true - Filtrar

    POST /tasks - Crear tarea

    PATCH /tasks/{id}/complete - Marcar completada

    PATCH /tasks/{id}/priority - Cambiar prioridad

Validaciones:

    title: mínimo 3 caracteres, sin caracteres especiales

    priority: entre 1 y 5

    due_date: no puede ser en el pasado
