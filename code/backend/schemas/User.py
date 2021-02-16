from typing import Optional

from . import ORMBaseSchema, Flair


class UserBase(ORMBaseSchema):
    email: str


# Separate data model for security purposes
class UserCreate(UserBase):
    password: str


class User(UserBase):
    flair: Optional[Flair]
    pass
