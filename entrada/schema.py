
from typing import Annotated
from contrib.schemas import BaseSchema_id
from pydantic import Field, PositiveInt

class EntradaSchema(BaseSchema_id):
    Url: Annotated[str, Field(description='URL da partida', example='https://www.futebol.com/partida/1234')]
    Nome: Annotated[str, Field(description='Nome do Time', example='Vasco')]
    Local: Annotated[str, Field(description='Local da partida, casa[A] ou fora[B]', example='A')]
    Robo: Annotated[PositiveInt, Field(description='Porcentagem Robô', example=50)]
    Povo: Annotated[PositiveInt, Field(description='Porcentagem Povo', example=50)]
    Ataque: Annotated[PositiveInt, Field(description='Porcentagem Ataque', example=50)]
    AtaqueP: Annotated[PositiveInt, Field(description='Porcentagem Ataque Perigoso', example=50)]
    Chute: Annotated[PositiveInt, Field(description='Porcentagem Chute', example=50)]
    Posse: Annotated[PositiveInt, Field(description='Porcentagem Posse de Bola', example=50)]
