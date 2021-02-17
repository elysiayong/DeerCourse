from typing import List

from .ORM import ORMBaseSchema
from .Program import Program


class Course(ORMBaseSchema):
    name: str
    description: str
    program: Program
    prerequisites: List["Course"] = []
    exclusions: List["Course"] = []
    corequisites: List["Course"] = []


Course.update_forward_refs()
