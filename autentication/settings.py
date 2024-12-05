from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer

security = HTTPBearer()

app = FastAPI()

API_KEY = "sua_chave_secreta_aqui" 

security = HTTPBearer()

def get_current_user(api_key: str = Depends(security)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"user_id": 1}  # Substitua por sua lógica para obter informações do usuário