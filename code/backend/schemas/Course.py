from typing import List, Optional

from pydantic import Field

from .ORM import ORMBaseSchema
from .Program import Program


class Course(ORMBaseSchema):
    code: str
    name: str
    description: str
    program: Optional[Program]


class CourseCreate(ORMBaseSchema):
    code: str
    name: str
    description: str
    program_code: Optional[str]


class CourseExtra(Course):
    prerequisites: Optional[str]
    exclusions: Optional[str]
    corequisites: Optional[str]
