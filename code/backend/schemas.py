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


class Review(BaseModel):
    review_id: int
    content: str
    user: User
    course: 'Course'
    user_rating: int

    # tags: List[Tag]
    class Config:
        orm_mode = True


class Course(BaseModel):
    name: str
    description: str
    prerequisites: List["Course"] = []
    exclusions: List["Course"] = []
    corequisites: List["Course"] = []
    program: 'Program'

    class Config:
        orm_mode = True


class Program(BaseModel):
    class Config:
        orm_mode = True

    name: str
    description: str


Course.update_forward_refs()  # To convert string-identified types to real references
