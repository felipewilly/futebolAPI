from contrib.schemas import BaseSchema
from pydantic import Field, PositiveInt, BaseModel
from typing import Annotated

class ProbabilidadeSchema(BaseSchema):
    Nome: Annotated[str, Field(description='Nome do Time', example='Vasco')]
    Soma_Media: Annotated[PositiveInt, Field(description='Soma das médias', example=50)]
    PB: Annotated[PositiveInt, Field(description='Probabilidade', example=50)]

class ProbabilidadeSchemaPublic(BaseModel):
    Nome: str
    Soma_Media: int
    PB: int