from msilib.schema import Media
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from contrib.models import BaseModel
from partida.model import PartidaModel
from entrada.model import EntradaModel

class ProbabilidadeModel(BaseModel):
    __tablename__ = 'probabilidade'

    Partida_id: Mapped[int] = mapped_column(Integer, ForeignKey('partida.pk_id'), nullable=False)
    Partida: Mapped['PartidaModel'] = relationship(back_populates='probabilidade', lazy='select')
    Entrada_id: Mapped[int] = mapped_column(Integer, ForeignKey('entrada.pk_id'), nullable=False)
    Entrada: Mapped['EntradaModel'] = relationship(back_populates='probabilidade', lazy='select')
    Media: Mapped[int] = mapped_column(Integer, nullable=False)
    Probabilidade: Mapped[int] = mapped_column(Integer, nullable=False)
