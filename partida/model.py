from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from contrib.models import BaseModel


class Partida(BaseModel):
    __tablename__ = 'partida'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)