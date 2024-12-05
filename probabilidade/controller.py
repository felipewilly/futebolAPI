<<<<<<< HEAD
from fastapi import APIRouter, HTTPException, status
from probabilidade.schema import ProbabilidadeSchemaPublic
from configs.dependencies import DatabaseDependency
from sqlalchemy.future import select
from entrada.model import EntradaModel
from probabilidade.model import ProbabilidadeModel
from tasks.matematica import *


router = APIRouter()

@router.get("/{id}", summary='Retorna a probabilidade', response_model=ProbabilidadeSchemaPublic)
async def get_probabilidade(id: int, db_session: DatabaseDependency):

    entrada_db: EntradaModel = (await db_session.execute(select(EntradaModel).filter(EntradaModel.partida_id == id).order_by(EntradaModel.pk_id.desc()))).scalars().first()

    if not entrada_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Entrada não encontrada ID: {id}")
    
    PAB = calcula_MEDIA(entrada_db.Ataque,  entrada_db.AtaqueP, entrada_db.Chute, entrada_db.Posse) 
    
    PBA_EQUIVALENCIA = calcula_EQ(entrada_db.Robo, entrada_db.Povo)

    PB = calcula_PAB(entrada_db.Robo, PB=PAB, PA=PBA_EQUIVALENCIA)

    pb = ProbabilidadeModel(partida_id=entrada_db.partida_id, entrada_id=entrada_db.pk_id, Nome=entrada_db.Nome, Soma_Media=PAB, PB=PB) # soma_media e pb são fixos por enquanto devido a faltado do calculeitor 2 etapa do projeto

    db_session.add(pb)
    await db_session.commit()

    return pb

=======
from fastapi import APIRouter, HTTPException, status
from probabilidade.schema import ProbabilidadeSchemaPublic
from configs.dependencies import DatabaseDependency
from sqlalchemy.future import select
from entrada.model import EntradaModel
from probabilidade.model import ProbabilidadeModel


router = APIRouter()

@router.get("/{id}", summary='Retorna a probabilidade', response_model=ProbabilidadeSchemaPublic)
async def get_probabilidade(id: int, db_session: DatabaseDependency):

    entrada_db: EntradaModel = (await db_session.execute(select(EntradaModel).filter_by(pk_id=id))).scalars().first()

    if not entrada_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Entrada não encontrada ID: {id}")

    #
    #calculeitor 2
    #

    pb = ProbabilidadeModel(partida_id=entrada_db.partida_id, entrada_id=entrada_db.pk_id, Nome=entrada_db.Nome, Soma_Media=50, PB=50) # soma_media e pb são fixos por enquanto devido a faltado do calculeitor 2 etapa do projeto

    db_session.add(pb)
    await db_session.commit()

    return pb

>>>>>>> 6cab4f90aa5a9639009bbda04b536276f927cff9
