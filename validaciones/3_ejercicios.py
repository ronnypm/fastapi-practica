from pydantic import BaseModel, Field, field_validator

# Ejemplo 2: Validar múltiples campos con la misma función


class Product(BaseModel):
    name: str = Field(min_length=5, max_length=50)
    description: str = Field(min_length=10, max_length=50)

    @field_validator("name", "description")
    @classmethod
    def no_empty(cls, value):
        if not value.strip():
            raise ValueError("No puede estar vacio")
        return value


product = Product(name="Monitor", description="Teros 32 pulgdas")
print(product)
