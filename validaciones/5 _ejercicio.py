# Diferencia entre fiel_valation,  model_validationfrom
from pydantic import BaseModel, model_validator
from pydantic import BaseModel, field_validator
from decimal import Decimal


class Product(BaseModel):
    price: Decimal
    discount: Decimal = Decimal("5.00")  # descuento por defecto

    @field_validator("discount", mode="after")
    @classmethod
    def apply_default_discount(cls, value):
        # Siempre aseguramos que tenga el descuento mínimo de 5
        return max(value, Decimal("5.00"))


print("-" * 30)


class Product(BaseModel):
    price: Decimal
    category: str
    discount: Decimal = Decimal("0")

    @model_validator(mode="after")
    @classmethod
    def conditional_discount(cls, model):
        if model.category == "Electronics" and model.price > 100:
            model.discount = Decimal("10.00")
        return model
