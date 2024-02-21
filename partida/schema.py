from typing import Annotated, Optional
from pydantic import Field, BaseModel, PositiveInt, ConfigDict
from contrib.schemas import BaseSchema, BaseSchema_id
from datetime import datetime


class PartidaSchema(BaseModel):

    Url: Annotated[Optional[str], Field(description='URL da partida', example='https://www.futebol.com/partida/1234', default=None)]
    Local: Annotated[str, Field(description='Local da partida, casa[A] ou fora[B]', example='A', max_length=1)]
    Robo: Annotated[PositiveInt, Field(description='Porcentagem Robô', example=50)]
    Povo: Annotated[PositiveInt, Field(description='Porcentagem Povo', example=50)]
    Agenda: Annotated[datetime, Field(description='Data e hora da partida', example='2024-02-13T20:00:00')]

class PartidaSchema_id(BaseSchema_id):

    Url: Annotated[Optional[str], Field(description='URL da partida', example='https://www.futebol.com/partida/1234', default=None)]
    Local: Annotated[str, Field(description='Local da partida, casa[A] ou fora[B]', example='A', max_length=1)]
    Robo: Annotated[PositiveInt, Field(description='Porcentagem Robô', example=50)]
    Povo: Annotated[PositiveInt, Field(description='Porcentagem Povo', example=50)]
    Agenda: Annotated[datetime, Field(description='Data e hora da partida', example='2024-02-13T20:00:00')]
    
    class Config:
        from_attributes = True

class PartidaSchema_update(BaseSchema):
    Url: Annotated[Optional[str], Field(description='URL da partida', example='https://www.futebol.com/partida/1234', default=None)]
