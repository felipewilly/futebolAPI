"""
Arquivo de dependências do FastAPI, conexão async com o banco de dados
"""

from typing import Annotated
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from configs.database import get_session
DatabaseDependency = Annotated[AsyncSession, Depends(get_session)]