from pydantic import BaseModel, Field, field_validator


class User(BaseModel):
    name: str = Field(min_length=4, max_length=20)

    @field_validator("name")
    @classmethod
    def any_name_here(cls, value):
        if any(char.isdigit() for char in value):
            raise ValueError("El nombre no debe contener numeros.")
        return value


user = User(name="juan")
