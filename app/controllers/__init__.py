from fastapi import APIRouter, FastAPI

from app.controllers import task, user

router = APIRouter(prefix='/api')


def init_app(app: FastAPI):
    for extension in (task, user):
        router.include_router(extension.router)
    app.include_router(router)
