from fastapi import FastAPI
from app.routers import app_futbolAPI

app = FastAPI()

app = FastAPI(title="Futebol-API", description="API de integração, para gerenciar partidas de futebol", version="0.1")
app.include_router(app_futbolAPI)