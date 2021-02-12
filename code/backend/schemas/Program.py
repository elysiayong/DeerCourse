from .ORM import ORMBaseModel


class Program(ORMBaseModel):
    name: str
    description: str
