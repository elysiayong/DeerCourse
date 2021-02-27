from .ORM import ORMBaseSchema


class Program(ORMBaseSchema):
    code: str
    name: str
