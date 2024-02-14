from typing import Annotated
from pydantic import BaseModel
from datetime import datetime, date

class BaseSchema(BaseModel):
    id: Annotated[int, "ID da entidade"]
    Created_at: Annotated[date, "Data de criação"]

class BaseSchemaID(BaseModel):
    id: int
