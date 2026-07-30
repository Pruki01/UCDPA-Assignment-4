from typing import List, Optional
from enum import Enum
from sqlalchemy import ForeignKey, String, Integer, Boolean, create_engine
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import session, login, session
class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class User(UserMixin, Base):
    __tablename__ = 'users'
    email:      Mapped[str]     = mapped_column(String(50))
    password:   Mapped[str]     = mapped_column(String(255), nullable=False)
    is_admin:   Mapped[bool]    = mapped_column(Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @login.user_loader
    def load_user(id):
        return session.get(User, int(id))

class ScreenType(Enum):
    Large   = 'Large'
    Medium  = 'Medium'
    Small   = 'Small'
class Screen(Base):
    __tablename__ = 'screens'

    type: Mapped[ScreenType] = mapped_column(SQLEnum(ScreenType))


class MovieGenre(Enum):
    ACTION      = 'Action'
    DRAMA       = 'Drama'
    HORROR      = 'Horror'
    COMEDY      = 'Comedy'
    Thriller    = 'Thriller'
class Movie(Base):
    __tablename__ = 'movies'

    title:      Mapped[str]          = mapped_column(String(50))
    genre:      Mapped[MovieGenre]   = mapped_column(SQLEnum(MovieGenre))
    duration:   Mapped[int]          = mapped_column(Integer)

Base.metadata.create_all(session.get_bind())