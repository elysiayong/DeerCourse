from . import ORMBaseModel


class UserBase(ORMBaseModel):
    email: str


# Separate data model for security purposes
class UserCreate(UserBase):
    password: str


class User(UserBase):
    # flair: Optional[Flair]
    pass
