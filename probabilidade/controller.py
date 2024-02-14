from fastapi import APIRouter
from probabilidade.schema import Probabilidade

router = APIRouter()

@router.get("/{id}", summary='Retorna a probabilidade')
def get_probabilidade(id: int):
    ...