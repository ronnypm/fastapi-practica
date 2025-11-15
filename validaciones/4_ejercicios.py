from pydantic import BaseModel, Field, field_validator
from decimal import Decimal
# Múltiples validadores para el mismo campo


class Product(BaseModel):
    price: Decimal

    @field_validator("price", mode="before")
    @classmethod
    def convert_to_decimal(cls, value):
        print(f"1.convet: {value}")
        return Decimal(str(value))

    @field_validator("price", mode="after")
    @classmethod
    def validate_decimal(cls, value):
        print(f"2. validate decimal: {value}")
        return value.quantize(Decimal("0.01"))


product = Product(price="10.4654654")
print(product.price)
