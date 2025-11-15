from pydantic import BaseModel, field_validator, Field


class Product(BaseModel):
    name: str = Field(min_length=2, max_length=10)

    @field_validator("name")
    @classmethod
    def validate_name(cls, name):
        print(f"Validate name {name}")


product = Product(name="Laasfdag")
