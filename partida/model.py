
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date
from contrib.models import BaseModel



class PartidaModel(BaseModel):
    __tablename__ = 'partidas'
    
    Url: Mapped[str] = mapped_column(String, nullable=True)
    Local: Mapped[str] = mapped_column(String(1), nullable=False)
    Robo: Mapped[int] = mapped_column(Integer, nullable=False)
    Povo: Mapped[int] = mapped_column(Integer, nullable=False)
    entrada: Mapped['EntradaModel'] = relationship(back_populates="partida")
    probabilidade: Mapped['ProbabilidadeModel'] = relationship(back_populates="partida")

