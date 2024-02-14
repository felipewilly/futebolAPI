from fastapi import APIRouter

router = APIRouter()

@router.get("/{id}", summary='Chama a entrada')
def get_entrada(id: int):
    return {"message": "Dados inseridos com sucesso!"}