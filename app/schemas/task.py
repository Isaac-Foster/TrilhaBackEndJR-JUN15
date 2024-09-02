from typing import Annotated
from datetime import datetime
from dataclasses import dataclass

from fastapi import Body, Query, HTTPException
from pydantic import BaseModel, StringConstraints
from sqlalchemy import update, select, delete

from app.constants.task import MaxLength, Status
from app.database import Session
from app import models


class TaskCreate(BaseModel):
    name: Annotated[
        str,
        StringConstraints(max_length=MaxLength.NAME),
        Body(description="name for task")
    ]
        
    description: Annotated[
        str,
        Body(description="describle your task")
    ]

    def insert(self, owner: str):
        with Session() as session:
            already = session.execute(
                select(models.task.Task).filter_by(name=self.name)
            ).fetchone()

        if not already:
            with Session() as session:
                task = models.task.Task(
                    name=self.name,
                    description=self.description,
                    owner=owner,
                    status=Status.DONE.value
                )
                session.add(task)
                session.commit()
                session.refresh(task)

            return task.__dict__


class Task(TaskCreate):
    owner: str
    created_at: datetime
    status: Status

    def update(self, owner, status):
        with Session() as session:
            is_auth = session.execute(
                select(models.task.Task)
                .filter_by(name=self.name, owner=self.owner)
            )

            if not is_auth:
                raise HTTPException(status_code=401, detail="user not auth")

            session.execute(
                update(task.Task)
                .values(status=status)
                .filter_by(name=self.name, owner=owner)
            )

            session.commit()
            return True


    def delete(self, owner, id):
         with Session() as session:
            is_auth = session.execute(
                select(task.Task)
                .filter_by(id=self.id, owner=self.owner)
            )

            if not is_auth:
                raise HTTPException(status_code=401, detail="user not auth")

            session.execute(
                delete(task.Task)
                .filter_by(name=self.id, owner=owner)
            )

            session.commit()
            return True
