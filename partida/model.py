<<<<<<< HEAD

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

=======

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
    Created_at: Mapped[date] = mapped_column(DateTime, nullable=False)
    Agenda: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    entrada: Mapped['EntradaModel'] = relationship(back_populates="partida")
    probabilidade: Mapped['ProbabilidadeModel'] = relationship(back_populates="partida")

>>>>>>> 6cab4f90aa5a9639009bbda04b536276f927cff9
