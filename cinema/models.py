from typing import List, Optional
from enum import Enum
from sqlalchemy import ForeignKey, String, Integer, Boolean, Date, Time
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
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
    screenings: Mapped[List['Screening']] = relationship(
        back_populates='screen',
        cascade='all, delete-orphan'
    )


class MovieGenre(Enum):
    ACTION      = 'Action'
    DRAMA       = 'Drama'
    HORROR      = 'Horror'
    COMEDY      = 'Comedy'
    Thriller    = 'Thriller'

class MovieStatus(Enum):
    CURRENT     = 'Current'
    SPECIAL     = 'Special'
    UPCOMING    = 'Upcoming'
class Movie(Base):
    __tablename__ = 'movies'

    title:      Mapped[str]                 = mapped_column(String(50))
    genre:      Mapped[MovieGenre]          = mapped_column(SQLEnum(MovieGenre))
    duration:   Mapped[int]                 = mapped_column(Integer)
    status:     Mapped[MovieStatus]         = mapped_column(SQLEnum(MovieStatus))
    image:      Mapped[str]                 = mapped_column(String(255)) 
    screenings: Mapped[List['Screening']]   = relationship(
        back_populates='movie',
        cascade='all, delete-orphan'
    )

class Screening(Base):
    __tablename__ = 'screenings'
    movie_id:   Mapped[int]     = mapped_column(ForeignKey('movies.id'))
    screen_id:  Mapped[int]     = mapped_column(ForeignKey('screens.id'))
    date:       Mapped[Date]    = mapped_column(Date)
    time:       Mapped[Time]    = mapped_column(Time)
    movies:     Mapped['Movie'] = relationship(
        back_populates='screening'
    )
    movies:     Mapped['Screen'] = relationship(
        back_populates='screening'
    )

Base.metadata.create_all(session.get_bind())