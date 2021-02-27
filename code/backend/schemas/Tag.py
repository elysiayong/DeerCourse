from .ORM import ORMBaseSchema


class Tag(ORMBaseSchema):
    id: int
    text: str
