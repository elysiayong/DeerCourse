from typing import List, Optional

from pydantic import Field

from .ORM import ORMBaseSchema
from .Program import Program


class Course(ORMBaseSchema):
    name: str
    description: str
    program: Program


class CourseCreate(ORMBaseSchema):
    name: str
    description: str
    program_name: str


class CourseExtra(Course):
    prerequisites: Optional[List[Course]]
    exclusions: Optional[str]
    corequisites: Optional[str]


class CourseInDB(Course):
    prerequisites: List["CourseInDB"] = []
    exclusions: List["CourseInDB"] = []
    corequisites: List["CourseInDB"] = []


CourseInDB.update_forward_refs()
