<<<<<<< HEAD
from typing import Annotated
from pydantic import BaseModel
from datetime import datetime, date

class BaseSchema(BaseModel):
    pass

class BaseSchema_id(BaseModel):
    pk_id: Annotated[int, "Identificador único"]

class Message(BaseModel):
=======
from typing import Annotated
from pydantic import BaseModel
from datetime import datetime, date

class BaseSchema(BaseModel):
    Created_at: Annotated[date, "Data de criação"]

class BaseSchema_id(BaseModel):
    pk_id: Annotated[int, "Identificador único"]

class Message(BaseModel):
>>>>>>> 6cab4f90aa5a9639009bbda04b536276f927cff9
    message: str