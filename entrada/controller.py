from fastapi import APIRouter
from sqlalchemy.future import select
from entrada.schema import EntradaSchema
from entrada.model import EntradaModel
from partida.model import PartidaModel
from contrib.schemas import Message
from configs.dependencies import DatabaseDependency

router = APIRouter()

@router.get("/{id}", summary='Chama a entrada',
            response_model=Message)
async def get_entrada(id: int, db_session: DatabaseDependency):


    return {"message": " sucesso!"}