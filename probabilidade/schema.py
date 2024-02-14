from contrib.schemas import BaseSchemaID
from pydantic import Field, PositiveInt
from typing import Annotated

class Probabilidade(BaseSchemaID):
    Nome: Annotated[str, Field(description='Nome do Time', example='Vasco')]
    Soma_Media: Annotated[PositiveInt, Field(description='Soma das médias', example=50)]
    Probabilidade: Annotated[PositiveInt, Field(description='Probabilidade', example=50)]
