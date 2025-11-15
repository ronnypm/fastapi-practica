Ejercicio 1

1. Modelo de Producto:

    id: entero único

    name: string (mínimo 3 caracteres, máximo 50)

    description: string opcional (máximo 200 caracteres)

    price: float (debe ser mayor a 0)

    stock: entero (no puede ser negativo)

    category: string que solo acepte valores: "electronics", "clothing", "food", "books"

    is_available: booleano (se calcula automáticamente: True si stock > 0)

2. Endpoints a implementar:

    GET /products/ - Listar todos los productos

    GET /products/{id} - Obtener un producto por ID

    GET /products/category/{category} - Filtrar productos por categoría

    POST /products/ - Crear un nuevo producto

    PATCH /products/{id}/stock - Actualizar solo el stock de un producto (recibe cantidad a sumar o restar)

3. Validaciones especiales:

    El precio debe tener máximo 2 decimales

    El nombre no debe contener números

    Al actualizar el stock, no puede quedar negativo

Pistas

    Usa Field de Pydantic para las validaciones

    Investiga @validator de Pydantic para validaciones personalizadas

    El método PATCH es para actualizaciones parciales

****