from .ORM import ORMBaseSchema


class Flair(ORMBaseSchema):
    flair_id: int
    text: str
