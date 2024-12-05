<<<<<<< HEAD
from sqlalchemy import Integer, String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from contrib.models import BaseModel


class ProbabilidadeModel(BaseModel):
    __tablename__ = 'probabilidades'
    
    entrada_id: Mapped[int] = mapped_column(Integer, ForeignKey('entradas.pk_id'), nullable=False)
    partida_id: Mapped[int] = mapped_column(Integer, ForeignKey('partidas.pk_id'), nullable=False)
    partida: Mapped['PartidaModel'] = relationship(back_populates="probabilidade", lazy='select')
    entrada: Mapped['EntradaModel'] = relationship(back_populates="probabilidade", lazy='select')
    Nome: Mapped[str] = mapped_column(String(255), nullable=False)
    Soma_Media: Mapped[float] = mapped_column(Float, nullable=False)
    PB: Mapped[float] = mapped_column(Float, nullable=False)
=======
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from contrib.models import BaseModel


class ProbabilidadeModel(BaseModel):
    __tablename__ = 'probabilidades'
    
    entrada_id: Mapped[int] = mapped_column(Integer, ForeignKey('entradas.pk_id'), nullable=False)
    partida_id: Mapped[int] = mapped_column(Integer, ForeignKey('partidas.pk_id'), nullable=False)
    partida: Mapped['PartidaModel'] = relationship(back_populates="probabilidade", lazy='select')
    entrada: Mapped['EntradaModel'] = relationship(back_populates="probabilidade", lazy='select')
    Nome: Mapped[str] = mapped_column(String(255), nullable=False)
    Soma_Media: Mapped[int] = mapped_column(Integer, nullable=False)
    PB: Mapped[int] = mapped_column(Integer, nullable=False)
>>>>>>> 6cab4f90aa5a9639009bbda04b536276f927cff9
