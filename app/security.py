import time

from fastapi import APIRouter, Response
from fastapi.security import OAuth2PasswordBearer

import jwt
from app.schemas.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


router = APIRouter()


class JWTManager:
    SESSION_TIME_LIMIT = 60 * 30

    SECRET = (
        "b83683c54a0221c51d67cabc4aff31172aff554b333bcb508237960acc26"
        "1687485a0429366157df36bb4911fcd4fd7173c6216d6e21a9633580f146"
        "7d19cb761b594f1c39d8792c6b2677254adf2132ac3ae00e57af3ef6f517"
        "2369501a3919ec5dafe6be239c5cc69ce383b8ecf24a25e47b65220f502b"
        "5bacb38df1ed6e8452e08624d07dbb7bf596f14bc8e973010a9c845d4c53"
        "d841ffcc4138f02123dcd6126421b97489216b229419062bab1660ec1ac5"
        "b12488629d14c005a0b86f324baa731babd04ef676b5262a79de596cbc91"
        "e59db719488d79f5c988e603241517a483b646b1fc326bce4260292daf5a"
        "79927b2d97ebb8765233222886102e55"
    )

    ALGORITHM = "HS256"

    @classmethod
    def create(cls, uid: int | str, issued_at: int = None,
               expires_at: int = None):
        if issued_at is None:
            issued_at = time.time()

        if expires_at is None:
            expires_at = time.time() + cls.SESSION_TIME_LIMIT

        return jwt.encode(
            dict(
                sub=uid,
                iat=issued_at,
                exp=expires_at
            ),
            cls.SECRET,
            algorithm=cls.ALGORITHM
        )

    @classmethod
    def decode(cls, token: str):
        return jwt.decode(token, cls.SECRET, algorithms=cls.ALGORITHM)


@router.post("/token")
async def signin(user: User, response: Response):
    if user.verify():
        token = JWTManager.create(uid=user.username)
        response.headers.append("Authorization", f"Bearer {token}")
        print(response.headers)

        return dict(
            access_token=token,
            type='Bearer'
        )
    return dict(message="Usuário ou Senha incorreta")

