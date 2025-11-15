from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional
from decimal import Decimal

# ==================== MODELOS ====================


class Product(BaseModel):
    """Modelo de producto con validaciones completas"""
    model_config = {"validate_assignment": True}

    id: int
    name: str = Field(min_length=3, max_length=50)
    # description: str | None = Field(None, max_length=200) (forma moderna)
    description: Optional[str] = Field(None, max_length=200)
    price: Decimal = Field(gt=0)  # ✅ AJUSTE 1: Decimal para dinero
    stock: int = Field(ge=0)
    category: str
    is_available: bool = True

    # Validación 1: Convertir a Decimal
    @field_validator("price", mode="before")
    @classmethod
    def convert_to_decimal(cls, v):
        """Convierte float o string a Decimal"""
        if isinstance(v, float):
            return Decimal(str(v))  # str() evita imprecisión de float
        return Decimal(v)

    # Validación 2: Nombre sin números
    @field_validator("name")
    @classmethod
    def name_no_number(cls, value):
        if any(char.isdigit() for char in value):
            raise ValueError("El nombre no debe contener números")
        return value

    # Validación 3: Precio con máximo 2 decimales
    @field_validator("price", mode="after")
    @classmethod
    def validate_price_decimals(cls, value: Decimal):
        if value.as_tuple().exponent < -2:
            raise ValueError("El precio solo puede tener hasta 2 decimales")
        return value.quantize(Decimal('0.01'))  # Redondea a 2 decimales

    # Validación 4: Categoría permitida
    @field_validator("category")
    @classmethod
    def validate_category(cls, value):
        allowed = ["electronics", "clothing", "food", "books"]
        if value not in allowed:
            raise ValueError(
                f"La categoría debe ser una de: {', '.join(allowed)}")
        return value

    # Validación 5: Stock y disponibilidad
    @model_validator(mode="after")
    def validate_stock_and_availability(self):
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo")
        self.is_available = self.stock > 0
        return self


class StockUpdate(BaseModel):
    """Modelo para actualizar stock (PATCH)"""
    quantity: int  # Puede ser positivo (agregar) o negativo (quitar)


# ==================== DATOS DE EJEMPLO ====================

product_list = [
    Product(id=1, name="Laptop Dell Inspiron", description="Laptop de alta gama con procesador Intel i7",
            price=899.99, stock=15, category="electronics", is_available=True),
    Product(id=2, name="iPhone Pro", description="Smartphone Apple última generación",
            price=1299.50, stock=8, category="electronics", is_available=True),
    Product(id=3, name="Camiseta Nike", description="Camiseta deportiva 100% algodón",
            price=29.99, stock=50, category="clothing", is_available=True),
    Product(id=4, name="Jeans Levis", description="Pantalón denim clásico azul",
            price=79.99, stock=30, category="clothing", is_available=True),
    Product(id=5, name="Pan Integral", description="Pan de trigo integral 500g",
            price=3.50, stock=100, category="food", is_available=True),
    Product(id=6, name="Leche Entera", description="Leche fresca entera 1 litro",
            price=2.99, stock=75, category="food", is_available=True),
    Product(id=7, name="Aceite de Oliva", description="Aceite extra virgen 500ml",
            price=12.99, stock=40, category="food", is_available=True),
    Product(id=8, name="Clean Code", description="Libro de Robert Martin sobre código limpio",
            price=45.00, stock=20, category="books", is_available=True),
    Product(id=9, name="Python Crash Course", description="Guía práctica para aprender Python",
            price=39.99, stock=25, category="books", is_available=True),
    Product(id=10, name="Mouse Logitech", description="Mouse inalámbrico ergonómico",
            price=25.99, stock=0, category="electronics", is_available=False),
    Product(id=11, name="Teclado Mecánico", description="Teclado RGB retroiluminado",
            price=89.99, stock=12, category="electronics", is_available=True),
    Product(id=12, name="Zapatillas Adidas", description="Zapatillas deportivas running",
            price=120.00, stock=18, category="clothing", is_available=True),
]

# ==================== ROUTER ====================

router = APIRouter(prefix="/products", tags=["products"])

# Diccionarios para búsqueda O(1)
product_dict: dict[int, Product] = {p.id: p for p in product_list}
category_dict: dict[str, list[Product]] = {}
for p in product_list:
    category_dict.setdefault(p.category, []).append(p)


# ==================== FUNCIONES AUXILIARES ====================

def search_product_by_id(product_id: int) -> Optional[Product]:
    """Busca un producto por ID"""
    return product_dict.get(product_id)


def search_product_by_category(category: str) -> Optional[list[Product]]:
    """Busca productos por categoría"""
    return category_dict.get(category)


# ==================== ENDPOINTS ====================

@router.get("/", status_code=status.HTTP_200_OK)
async def get_products():
    """Obtiene todos los productos"""
    return product_list


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_product_by_id(id: int):
    """Obtiene un producto por ID"""
    product = search_product_by_id(id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )
    return product


# ✅ AJUSTE 2: Query parameters para filtrado (más flexible)
@router.get("/filter/by-category", status_code=status.HTTP_200_OK)
async def get_products_by_category(category: str):
    """
    Filtra productos por categoría usando query parameter.
    URL ejemplo: /products/filter/by-category?category=electronics
    """
    products = search_product_by_category(category)
    if products is None or len(products) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encontraron productos en la categoría '{category}'"
        )
    return products


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    """Crea un nuevo producto"""
    if search_product_by_id(product.id) is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El producto ya existe"
        )

    # Agregar a todas las estructuras de datos
    product_list.append(product)
    product_dict[product.id] = product
    category_dict.setdefault(product.category, []).append(product)

    return product


@router.patch("/{id}/stock", status_code=status.HTTP_200_OK)
async def update_stock(id: int, stock_update: StockUpdate):
    """
    Actualiza el stock de un producto (suma o resta cantidad).
    Ejemplos:
    - {"quantity": 10}  → Agrega 10 unidades
    - {"quantity": -5}  → Quita 5 unidades
    """
    product = search_product_by_id(id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    # Calcular nuevo stock
    new_stock = product.stock + stock_update.quantity

    # ✅ AJUSTE 3: Validación explícita ANTES de asignar
    # Esto da error 400 claro, en lugar de 500 del validator de Pydantic
    if new_stock < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Stock insuficiente. Stock actual: {product.stock}, intentas quitar: {abs(stock_update.quantity)}"
        )

    # Actualizar producto
    product.stock = new_stock
    product.is_available = new_stock > 0

    return product
