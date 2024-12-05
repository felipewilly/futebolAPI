<<<<<<< HEAD
from contrib.schemas import BaseSchema
from pydantic import Field, PositiveInt, BaseModel, PositiveFloat
from typing import Annotated

class ProbabilidadeSchema(BaseSchema):
    Nome: Annotated[str, Field(description='Nome do Time', example='Vasco')]
    Soma_Media: Annotated[PositiveFloat, Field(description='Soma das médias', example=50)]
    PB: Annotated[PositiveFloat, Field(description='Probabilidade', example=50)]

class ProbabilidadeSchemaPublic(BaseModel):
    Nome: str
    Soma_Media: float
    PB: float
=======
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
>>>>>>> 6cab4f90aa5a9639009bbda04b536276f927cff9
