from msilib.schema import Media
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from contrib.models import BaseModel


class ProbabilidadeModel(BaseModel):
    __tablename__ = 'probabilidades'

    partida: Mapped['PartidaModel'] = relationship(back_populates="probabilidade", lazy='select')
    partida_id: Mapped[int] = mapped_column(Integer, ForeignKey('partidas.pk_id'), nullable=False)
    entrada: Mapped['EntradaModel'] = relationship(back_populates="probabilidade", lazy='select')
    entrada_id: Mapped[int] = mapped_column(Integer, ForeignKey('entradas.pk_id'), nullable=False)
    Nome: Mapped[str] = mapped_column(String(255), nullable=False)
    Soma_Media: Mapped[int] = mapped_column(Integer, nullable=False)
    PB: Mapped[int] = mapped_column(Integer, nullable=False)
