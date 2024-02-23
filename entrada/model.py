
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from contrib.models import BaseModel



class EntradaModel(BaseModel):
    __tablename__ = 'entradas'

    partida: Mapped['PartidaModel'] = relationship(back_populates="entrada", lazy='select')
    partida_id: Mapped[int] = mapped_column(Integer, ForeignKey("partidas.pk_id"), nullable=False)
    Url: Mapped[str] = mapped_column(String, nullable=False)
    Nome: Mapped[str] = mapped_column(String(255), nullable=False)
    Local: Mapped[str] = mapped_column(String(1), nullable=False)
    Robo: Mapped[int] = mapped_column(Integer, nullable=False)
    Povo: Mapped[int] = mapped_column(Integer, nullable=False)
    Ataque: Mapped[int] = mapped_column(Integer, nullable=False)
    AtaqueP: Mapped[int] = mapped_column(Integer, nullable=False)
    Posse: Mapped[int] = mapped_column(Integer, nullable=False)
    Chute: Mapped[int] = mapped_column(Integer, nullable=False)
    probabilidade: Mapped['ProbabilidadeModel'] = relationship(back_populates="entrada")

    
