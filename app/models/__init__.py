from fastapi import FastAPI

from app.database import engine, Base
from app.models import task, user  # noqa


def init_app(app: FastAPI): 
    Base.metadata.create_all(engine)
