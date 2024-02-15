from typing import Annotated
from pydantic import BaseModel
from datetime import datetime, date

class BaseSchema(BaseModel):
    Created_at: Annotated[date, "Data de criação"]

