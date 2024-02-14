from fastapi import APIRouter, HTTPException, status
from partida.schema import Partida, PartidaOut


router = APIRouter()

@router.post("/",
    summary='Cria uma nova partida',
    response_model=Partida)
def post_partida(partida: Partida):
    ...

@router.get("/{id}", summary='Retorna uma partida', 
            response_model=PartidaOut)
def get_partida(id: int):
    ...