from typing import Annotated
from pydantic import BaseModel
from datetime import datetime, date

class BaseSchema(BaseModel):
    id: int
    Created_at: date