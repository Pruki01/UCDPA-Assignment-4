from typing import List
from enum import Enum
from sqlalchemy import ForeignKey, String, Integer, Boolean, Date, Time, DateTime, Float, Text
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import session, login, session

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class User(UserMixin, Base):
    __tablename__ = 'users'
    email:      Mapped[str]             = mapped_column(String(50))
    password:   Mapped[str]             = mapped_column(String(255), nullable=False)
    is_admin:   Mapped[bool]            = mapped_column(Boolean, default=False)
    orders:     Mapped[List['Order']]   = relationship(
        back_populates='user',
        cascade='all, delete-orphan'
    )

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

    title:          Mapped[str]                 = mapped_column(String(50))
    genre:          Mapped[MovieGenre]          = mapped_column(SQLEnum(MovieGenre))
    description:    Mapped[str]                 = mapped_column(Text)
    duration:       Mapped[int]                 = mapped_column(Integer)
    status:         Mapped[MovieStatus]         = mapped_column(SQLEnum(MovieStatus))
    image:          Mapped[str]                 = mapped_column(String(255)) 
    screenings:     Mapped[List['Screening']]   = relationship(
        back_populates='movie',
        cascade='all, delete-orphan'
    )

class Screening(Base):
    __tablename__ = 'screenings'
    movie_id:   Mapped[int]         = mapped_column(ForeignKey('movies.id'))
    screen_id:  Mapped[int]         = mapped_column(ForeignKey('screens.id'))
    date:       Mapped[Date]        = mapped_column(Date)
    time:       Mapped[Time]        = mapped_column(Time)
    movie:      Mapped['Movie']     = relationship(
        back_populates='screenings'
    )
    screen:     Mapped['Screen']    = relationship(
        back_populates='screenings'
    )
    tickets:    Mapped[List['Ticket']]    = relationship(
        back_populates='screening',
        cascade='all, delete-orphan'
    )

class TicketType(Enum):
    ADULT   = 'Adult'
    CHILD   = 'Child'
    STUDENT = 'Student'

class TicketPrice(Enum):
    ADULT   = 10.99
    CHILD   = 8.99
    STUDENT = 9.99

class Ticket(Base):
    __tablename__ = 'tickets'

    screening_id:   Mapped[int]         = mapped_column(ForeignKey('screenings.id'))
    order_id:       Mapped[int]         = mapped_column(ForeignKey('orders.id'))
    ordered:        Mapped[DateTime]    = mapped_column(DateTime)
    seat:           Mapped[str]         = mapped_column(String(3))
    type:           Mapped[TicketType]  = mapped_column(SQLEnum(TicketType))
    price:          Mapped[Float]       = mapped_column(Float)
    screening:      Mapped['Screening'] = relationship(
        back_populates='tickets'
    )
    order:          Mapped['Order']     = relationship(
        back_populates='tickets'
    )

class Order(Base):
    __tablename__ = 'orders'

    user_id:    Mapped[int]             = mapped_column(ForeignKey('users.id'))

    user:       Mapped['User']          = relationship(
        back_populates='orders'
    )
    tickets:     Mapped[List['Ticket']] = relationship(
        back_populates='order',
        cascade='all, delete-orphan'
    )

Base.metadata.create_all(session.get_bind())

