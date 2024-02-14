from sqlalchemy.orm import DeclarativeBase, Mapped

class BaseModel(DeclarativeBase):
    id: Mapped[int]