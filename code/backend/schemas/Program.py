from .ORM import ORMBaseSchema
from typing import Optional, List


class Program(ORMBaseSchema):
    code: str
    name: str


class ProgramUpdate(ORMBaseSchema):
    name: Optional[str]


class Programs(ORMBaseSchema):
    """
    List of Program objects
    """
    __root__: List[Program]
