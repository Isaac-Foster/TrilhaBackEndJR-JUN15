import re
import string
from typing import Annotated

from fastapi import Body, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
import bcrypt

from app.database import Session
from app import models


class WeakPasswordError(HTTPException):
    """Exceção levantada para senhas fracas."""

    def __init__(self, passwd: str, message: str = "Senha é muito fraca"):
        self.password = passwd
        self.message = message
        super().__init__(status_code=400, detail=self.message)

    def __str__(self):
        return f'{self.message}: {self.password}'


def is_strong_pass(passwd: str,
                   chars: int = 8,
                   lowers: int = 3,
                   uppers: int = 1,
                   digits: int = 1):

    is_strong = re.search(
        (
            "(?=^.{%i,}$)"
            "(?=.*[a-z]{%i,})"
            "(?=.*[A-Z]{%i})"
            "(?=.*[0-9]{%i,})"
            "(?=.*[%s}]+)"
        ) % 
        (
            chars, lowers, uppers,
            digits, re.escape(string.punctuation)
        ),
        passwd
    )

    if not is_strong:
        if len(passwd) < chars:
            raise WeakPasswordError(passwd, f"A senha deve ter pelo menos {chars} caracteres")
        if not any(char.isdigit() for char in passwd):
            raise WeakPasswordError(passwd, "A senha deve conter pelo menos um dígito")
        if not any(char.isupper() for char in passwd):
            raise WeakPasswordError(passwd, "A senha deve conter pelo menos uma letra maiúscula")
        if not any(char.islower() for char in passwd):
            raise WeakPasswordError(passwd, "A senha deve conter pelo menos uma letra minúscula")
        if not any(char in string.punctuation for char in passwd):
            raise WeakPasswordError(passwd, "A senha deve conter pelo menos um caractere especial")
    return True


class UserCreate(BaseModel):
    username: Annotated[str, Body(description="@username")]
    password: Annotated[str, Body(description="Password21@#")]

    def registry(self):
        is_strong_pass(self.password)

        salt = bcrypt.gensalt()

        hashed = bcrypt.hashpw(self.password.encode('utf-8'), salt)

        with Session() as session:
            already = session.execute(
                select(models.user.User).filter_by(username=self.username)
            ).scalar()

        if not already:
            with Session() as session:
                session.add(models.user.User(
                    username=self.username,
                    password=hashed
                ))
                session.commit()

            return True

        return False


class User(UserCreate):
    def verify(self) -> bool:
        with Session() as session:
            hashed = session.execute(
                select(models.user.User.password)
                .filter_by(username=self.username)
            ).fetchone()

        if not hashed:
            return False

        return bcrypt.checkpw(
            self.password.encode(),
            hashed[0]
        )


class Token(BaseModel):
    access_token: str
    token_type: str
