from typing import List

from .ORM import ORMBaseModel
from .Program import Program


class Course(ORMBaseModel):
    name: str
    description: str
    prerequisites: List["Course"] = []
    exclusions: List["Course"] = []
    corequisites: List["Course"] = []
    program: Program


Course.update_forward_refs()
