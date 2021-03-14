from .ORM import ORMBaseSchema
from typing import List


class TagCreate(ORMBaseSchema):
    text: str


class Tag(TagCreate):
    tag_id: int


class Tags(ORMBaseSchema):
    """
    List of Tag objects
    """
    __root__: List[Tag]
