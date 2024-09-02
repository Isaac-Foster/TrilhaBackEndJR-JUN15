from enum import Enum


class MaxLength(Enum):
    NAME = 256
    DESCRIPTION = 500
    STATUS = 5


class Status(Enum):
    DOING = 'doing'
    TODO = 'todo'
    DONE = 'done'
