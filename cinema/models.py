from typing import List, Optional
from sqlalchemy import ForeignKey, String, Integer, Boolean, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import session, login, session
class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class User(UserMixin, Base):
    __tablename__ = 'users'
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @login.user_loader
    def load_user(id):
        return session.get(User, int(id))

Base.metadata.create_all(session)