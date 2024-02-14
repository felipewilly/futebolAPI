from typing import Annotated
from pydantic import Field, BaseModel, PositiveInt
from contrib.schemas import BaseSchema
from datetime import datetime


class Partida(BaseModel):
    Url: Annotated[str, Field(description='URL da partida', example='https://www.futebol.com/partida/1234')]
    Local: Annotated[str, Field(description='Local da partida, casa[A] ou fora[B]', example='A', max_length=1)]
    Robo: Annotated[PositiveInt, Field(description='Porcentagem Robô', example=50)]
    Povo: Annotated[PositiveInt, Field(description='Porcentagem Povo', example=50)]
    Agenda: Annotated[datetime, Field(description='Data e hora da partida', example='2024-02-13T20:00:00')]
    
class PartidaOut(Partida, BaseSchema):
    class Config:
        extra = 'forbid'
        from_atrributes = True
