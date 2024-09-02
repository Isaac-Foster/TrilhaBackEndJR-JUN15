from sqlalchemy import Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String(256), nullable=False)
