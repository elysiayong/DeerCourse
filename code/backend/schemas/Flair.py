from .ORM import ORMBaseSchema


class Flair(ORMBaseSchema):
    id: int
    text: str
