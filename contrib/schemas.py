from typing import Annotated
from pydantic import BaseModel
from datetime import datetime, date

class BaseSchema(BaseModel):
    pass

class BaseSchema_id(BaseModel):
    pk_id: Annotated[int, "Identificador único"]

class Message(BaseModel):
    message: str