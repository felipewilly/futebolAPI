from fastapi import APIRouter
from probabilidade.schema import ProbabilidadeSchema
from configs.dependencies import DatabaseDependency
from sqlalchemy.future import select
from entrada.model import EntradaModel
from probabilidade.model import ProbabilidadeModel


router = APIRouter()

@router.get("/{id}", summary='Retorna a probabilidade', response_model=ProbabilidadeSchema)
async def get_probabilidade(id: int, db_session: DatabaseDependency):

    entrada_db: EntradaModel = (await db_session.execute(select(EntradaModel).filter_by(pk_id=id))).scalars().first()

    pb = ProbabilidadeModel(partida_id=entrada_db.partida_id, entrada_id=entrada_db.pk_id, Media=50, Probabilidade=50) 
    db_session.add(pb)
    await db_session.commit()

    return pb

