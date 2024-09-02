"""
POST /task
    Criar a tarefa.
    JSON:
        name: str
        description: str


DELETE /task
    Deletar a tarefa.

    JSON:
        id: int
"""
from typing import Annotated
from http import HTTPStatus

from fastapi import APIRouter, Query, Depends, Response, Header
from fastapi.exceptions import HTTPException
import jwt

from app.schemas.task import TaskCreate, Task
from app.security import oauth2_scheme, JWTManager


router = APIRouter(prefix='/task', tags=["task"])

@router.post('')
async def create(
    response: Response,
    task_create: TaskCreate,
    token: str = Depends(oauth2_scheme)
    ):

    try:
        payload = JWTManager.decode(token)
        print(payload)

    except jwt.exceptions.DecodeError:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN
        )

    task = task_create.insert(payload['sub']) or {}

    if not task:
        response.status_code = HTTPStatus.CONFLICT

    return task


@router.get('')
async def read(id: Annotated[int | str, Query(description="task id")],
               token: str = Depends(oauth2_scheme)):
    try:
        payload = JWTManager.decode(token)
    except jwt.exceptions.DecodeError:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN
        )

    raise NotImplementedError


@router.put('')
async def update():
    return


@router.delete('')
async def delete():
    return
