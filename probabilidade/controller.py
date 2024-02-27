from fastapi import APIRouter
from probabilidade.schema import ProbabilidadeSchemaPublic
from configs.dependencies import DatabaseDependency
from sqlalchemy.future import select
from entrada.model import EntradaModel
from probabilidade.model import ProbabilidadeModel



router = APIRouter()

@router.get("/{id}", summary='Retorna a probabilidade', response_model=ProbabilidadeSchemaPublic)
async def get_probabilidade(id: int, db_session: DatabaseDependency):

    entrada_db: EntradaModel = (await db_session.execute(select(EntradaModel).filter_by(pk_id=id))).scalars().first()
    pb = ProbabilidadeModel(partida_id=entrada_db.partida_id, entrada_id=entrada_db.pk_id, Nome=entrada_db.Nome, Soma_Media=50, PB=50) # soma_media e pb são fixos por enquanto devido a faltado do calculeitor 2 etapa do projeto
    db_session.add(pb)
    await db_session.commit()

    return pb

