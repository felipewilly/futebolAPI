
from fastapi import APIRouter, HTTPException, status, Body
from sqlalchemy.future import select
from partida.schema import PartidaSchema, PartidaSchema_id, PartidaSchema_update
from contrib.schemas import Message
from partida.model import PartidaModel
from configs.dependencies import DatabaseDependency

router = APIRouter()

@router.post("/",
    summary='Cria uma nova partida',
    status_code=status.HTTP_201_CREATED,
    response_model=Message)
async def post_partida(db_session: DatabaseDependency, partida: PartidaSchema = Body(...)):

    partida_db = PartidaModel(**partida.model_dump())

    db_session.add(partida_db)
    await db_session.commit()
    await db_session.refresh(partida_db)

    return {'message': f'Partida criada com sucesso ID {partida_db.pk_id}'}

@router.get("/all", 
    summary='Retorna Varias partidas', 
    response_model=list[PartidaSchema_id])
async def get_all_partida(db_session: DatabaseDependency, skip: int = 0, limit: int = 100 ):

    partidas_db = (await db_session.execute(select(PartidaModel).offset(skip).limit(limit))).scalars().all()

    return partidas_db
    
@router.get("/{id}", 
    summary='Retorna uma partida',
    status_code=status.HTTP_200_OK,
    response_model=PartidaSchema_id)
async def get_partida(id: int, db_session: DatabaseDependency):

    partida_db: PartidaSchema_id = (await db_session.execute(select(PartidaModel).filter_by(pk_id=id))).scalars().first()

    return partida_db

@router.patch("/{id}", summary='Atualiza uma partida', 
            response_model=Message)
async def update_partida(id: int, db_session: DatabaseDependency, partida_up: PartidaSchema_update = Body(...)):

    partida_db: PartidaSchema = (await db_session.execute(select(PartidaModel).filter_by(pk_id=id))).scalars().first() 

    partida_update =  partida_up.model_dump()
    
    for key, value in partida_update.items():
        setattr(partida_db, key, value)

    await db_session.commit()
    await db_session.refresh(partida_db)

    return {'message': f'Partida atualizada com sucesso ID {partida_db.pk_id}, Nova URL {partida_db.Url}'}