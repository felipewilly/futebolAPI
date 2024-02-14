from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer


class BaseModel(DeclarativeBase):
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)