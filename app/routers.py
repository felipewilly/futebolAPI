from fastapi import APIRouter
from partida.controller import router as partida
from entrada.controller import router as entrada
from probabilidade.controller import router as probabilidade

app_futbolAPI = APIRouter()
app_futbolAPI.include_router(partida, prefix='/partida', tags=['Partida'])
app_futbolAPI.include_router(entrada, prefix='/entrada', tags=['Entrada'])
app_futbolAPI.include_router(probabilidade, prefix='/probabilidade', tags=['Probabilidade'])