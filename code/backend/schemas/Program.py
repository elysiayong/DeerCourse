from .ORM import ORMBaseSchema


class Program(ORMBaseSchema):
    name: str
    description: str
