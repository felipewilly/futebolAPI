from fastapi import APIRouter, HTTPException, status, Body
from partida.schema import PartidaSchema
from partida.model import PartidaModel
from configs.dependencies import DatabaseDependency

router = APIRouter()

@router.post("/",
    summary='Cria uma nova partida',
    response_model=PartidaSchema)
async def post_partida(db_session: DatabaseDependency, partida: PartidaSchema):

    partida_db = PartidaModel(**partida.model_dump())

    db_session.add(partida_db)
    await db_session.commit()
    return partida_db


@router.get("/{id}", summary='Retorna uma partida', 
            response_model=PartidaSchema)
def get_partida(id: int):
    ...

@router.put("/{id}", summary='Atualiza uma partida', 
            response_model=PartidaSchema)
def update_partida(id: int):
    ...