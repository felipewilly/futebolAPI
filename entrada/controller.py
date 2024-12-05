from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.future import select
from entrada.model import EntradaModel
from partida.model import PartidaModel
from contrib.schemas import Message
from configs.dependencies import DatabaseDependency
from tasks.coletor import raspagem
from autentication.settings import get_current_user

from entrada.validation import Partida_Vasco, check_url # temporario para testar partida sem o coletor

router = APIRouter()

@router.get("/{id}", summary='Chama a entrada',
            response_model=Message)
async def get_entrada(id: int, db_session: DatabaseDependency,):

    partida_db: PartidaModel = (await db_session.execute(select(PartidaModel).filter_by(pk_id=id))).scalars().first()

    if not partida_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Partida não encontrada ID: {id}")

    if partida_db.Url == '':
        return {"message": f"Partida sem url, por favor atualizar ID: {partida_db.pk_id}"}

    corretor = str(partida_db.Local).upper()
    coletor = await raspagem(url=partida_db.Url, alt=corretor) 
    

    entrada = EntradaModel( Nome=coletor['Nome'],
                            Posse=coletor['Posse'],
                            Ataque=coletor['Ataque'],
                            AtaqueP=coletor['AtaqueP'],
                            Chute=coletor['Chute'],
                            partida_id=partida_db.pk_id, 
                            Url=partida_db.Url, 
                            Local=partida_db.Local, 
                            Robo=partida_db.Robo, 
                            Povo=partida_db.Povo)
    db_session.add(entrada)

    await db_session.commit()

    return {"message": "chamada com sucesso!"}
