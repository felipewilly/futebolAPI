import os
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(default=os.getenv('DB_URL', 'postgresql+asyncpg://postgres:postgres@localhost/Fastapi'))


settings = Settings()