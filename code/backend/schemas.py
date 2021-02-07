from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


# Separate data model for security purposes
class UserCreate(UserBase):
    password: str


class User(UserBase):
    # flair: Optional[Flair]
    class Config:
        orm_mode = True
