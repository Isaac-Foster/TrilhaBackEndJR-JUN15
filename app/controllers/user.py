from fastapi import APIRouter, Response
from app.schemas.user import UserCreate, User
from app.security import JWTManager

router = APIRouter(prefix='/user', tags=["user"])


@router.post('/signup')
async def signup(create: UserCreate):
    if create.registry():
        return dict(message="Login criado com sucesso")
    return False


@router.post('/signin')
async def signin(user: User, response: Response):
    if user.verify():
        return dict(
            access_token=JWTManager.create(uid=user.username),
            type='Bearer'
        )
    return dict(message="Usuário ou Senha incorreta")


