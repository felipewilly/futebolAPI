<<<<<<< HEAD
from fastapi import FastAPI
from app.routers import app_futbolAPI


app = FastAPI()

app = FastAPI(title="Futebol-API", description="API de integração, para gerenciar partidas de futebol", version="0.1")
app.include_router(app_futbolAPI)

=======
from fastapi import FastAPI
from app.routers import app_futbolAPI

app = FastAPI()

app = FastAPI(title="Futebol-API", description="API de integração, para gerenciar partidas de futebol", version="0.1")
app.include_router(app_futbolAPI)
>>>>>>> 6cab4f90aa5a9639009bbda04b536276f927cff9
