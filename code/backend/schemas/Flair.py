from .ORM import ORMBaseModel


class Flair(ORMBaseModel):
    id: int
    text: str
