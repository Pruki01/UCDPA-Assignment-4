from typing import List, Optional
from sqlalchemy import ForeignKey, String, Integer, Boolean, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

engine = create_engine('postgresql+psycopg2://test:test@localhost:5432/cinema')
class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class User(Base):
    __tablename__ = 'users'
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean)

Base.metadata.create_all(engine)