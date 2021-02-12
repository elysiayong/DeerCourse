from typing import List

from .Program import Program
from .ORM import ORMBaseModel


class Course(ORMBaseModel):
    name: str
    description: str
    prerequisites: List["Course"] = []
    exclusions: List["Course"] = []
    corequisites: List["Course"] = []
    program: Program


Course.update_forward_refs()
