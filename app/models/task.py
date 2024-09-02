from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.constants.task import MaxLength
from app.database import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(MaxLength.NAME.value), nullable=False)
    description = Column(String(MaxLength.DESCRIPTION.value), nullable=False)
    owner = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    status = Column(String(MaxLength.STATUS.value), nullable=False)
