from .ORM import ORMBaseModel


class Tag(ORMBaseModel):
    id: int
    text: str
