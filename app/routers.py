from fastapi import APIRouter
from partida.controller import router as partida

app_futbolAPI = APIRouter()
app_futbolAPI.include_router(partida, prefix='/partida', tags=['Partida'])